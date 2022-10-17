from urllib.request import Request, urlopen
import json
import re

from Team import Team
from Pokemon import Pokemon

class Match():
	def __init__(self, url):
		self.__url = url
		self.__raw_data = ''
		self.__log = ''
		self.__teams = {}
		self.__team_numbers = ['1', '2']

	def parseData(self):
		self.__getRawData()
		self.__getPokemon()
		self.__getPokemonNicknames()
		self.__getPokemonMegaNames()
		self.__getDeaths()
		self.__getDirectKills()
		self.__getIndirectKills()

	def print(self):
		for number in self.__team_numbers:
			for pokemon in self.__teams[number].pokemon.values():
				print(pokemon)
			print()

	def toString(self):
		out = ''
		for number in self.__team_numbers:
			for pokemon in self.__teams[number].pokemon.values():
				out += str(pokemon) + '\n'
			out += '\n'
		return out

	def __getRawData(self):
		req = Request(url=self.__url, headers={'User-Agent': 'Mozilla/5.0'})
		self.__raw_data = json.loads(urlopen(req).read())
		self.__log = self.__raw_data['log']
		for number in self.__team_numbers:
			self.__teams[number] = Team()
			self.__teams[number].coach = self.__raw_data['p' + number]

	def __getPokemon(self):
		log_copy = self.__log
		for number in self.__team_numbers:
			while ('poke|p' + number + '|' in log_copy):
				name = log_copy.split('poke|p' + number + '|', 1)[1].split('|', 1)[0].split(',', 1)[0]
				self.__teams[number].pokemon[name] = Pokemon(name)
				log_copy = log_copy.split(name, 1)[1]

	def __getPokemonNicknames(self):
		for number in self.__team_numbers:
			for pokemon in self.__teams[number].pokemon.keys():
				self.__getNickname(pokemon, number)

	def __getNickname(self, pokemon, team_number):
		log_copy = self.__log
		while (pokemon in log_copy or pokemon.replace('-*', '') in log_copy):
			name_match = \
			log_copy.split('p' + team_number + 'a: ', 1)[1].split('|', 1)[1].split('|', 1)[0].split(',', 1)[0]
			if (name_match == pokemon or re.compile(r'{}'.format(pokemon)).search(name_match)):
				nickname = log_copy.split('p' + team_number + 'a: ', 1)[1].split('|', 1)[0].split('-')[0]
				if ('-' in name_match):
					self.__teams[team_number].pokemon[pokemon].name = name_match
				self.__teams[team_number].pokemon[pokemon].nickname = nickname
				self.__teams[team_number].nickname_map[nickname] = pokemon
				return
			log_copy = log_copy.split('p' + team_number + 'a: ', 1)[1]

	def __getPokemonMegaNames(self):
		for number in self.__team_numbers:
			for pokemon in self.__teams[number].pokemon.keys():
				self.__getMegaName(pokemon, number)

	def __getMegaName(self, pokemon, team_number):
		log_copy = self.__log
		while (pokemon + '-Mega' in log_copy):
			if (log_copy.split(pokemon + '-Mega', 1)[0].split('|p')[-1].split('a: ')[0] == team_number):
				self.__teams[team_number].pokemon[pokemon].mega_name = pokemon + '-Mega' + \
				                                                       log_copy.split(pokemon + '-Mega', 1)[1].split(
					                                                       ',')[0]
			log_copy = log_copy.split(pokemon + '-Mega', 1)[1]

	def __getDeaths(self):
		log_copy = self.__log
		while ('faint|p' in log_copy):
			team_number = log_copy.split('faint|p', 1)[1].split('a:', 1)[0]
			pokemon = log_copy.split('faint|p', 1)[1].split(': ', 1)[1].split('\n|', 1)[0]
			self.__teams[team_number].getPokemonWithNickname(pokemon).dead = True
			log_copy = log_copy.split('faint|p', 1)[1]

	def __getDirectKills(self):
		log_copy = self.__log
		while ('0 fnt\n' in log_copy):
			fainted_team = log_copy.split('0 fnt\n', 1)[0].split('|p')[-1].split('a:', 1)[0]
			killer_team = '1' if fainted_team == '2' else '2'
			killer_turn = log_copy.split('0 fnt\n', 1)[0].split('|p' + killer_team + 'a:')[-1]
			# Check for Future Sight
			if ('move: Future Sight' in killer_turn or 'move: Doom Desire' in killer_turn):
				move = killer_turn.split('move: ')[-1].split('\n')[0]
				killer_pokemon = \
				log_copy.split('0 fnt\n', 1)[0].split('|move: ' + move)[-3].split('|p' + killer_team + 'a: ')[-1]
				self.__teams[killer_team].getPokemonWithNickname(killer_pokemon).direct_kills += 1
			else:
				killer_pokemon = log_copy.split('0 fnt\n', 1)[0].split('|p' + killer_team + 'a: ')[-1].split('|', 1)[0]
				self.__teams[killer_team].getPokemonWithNickname(killer_pokemon).direct_kills += 1
			log_copy = log_copy.split('0 fnt\n', 1)[1]

	def __getIndirectKills(self):
		log_copy = self.__log
		while ('0 fnt|[' in log_copy):
			fainted_pokemon = log_copy.split('|0 fnt|[', 1)[0].split('a: ')[-1]
			fainted_pokemon_team = log_copy.split('|0 fnt|[', 1)[0].split('|p')[-1].split('a:')[0]
			killer_pokemon_team = '1' if fainted_pokemon_team == '2' else '2'
			passive_reason = log_copy.split('|0 fnt|[from] ', 1)[1].split('\n|', 1)[0].split('|', 1)[0]

			# Check for an indirect kill based on status
			if (passive_reason == 'psn' or passive_reason == 'brn'):
				killer_turn = log_copy.split('-status|p' + fainted_pokemon_team + 'a: ' + fainted_pokemon)[-2]
				if (killer_turn.split('|p' + fainted_pokemon_team + 'a: ' + fainted_pokemon)[-2].split('|')[1]
						== 'switch'):
					self.__addIndirectKill(killer_pokemon_team, self.__getHazardSetter(killer_pokemon_team,
					                                                                   'Toxic Spikes'))
				else:
					self.__addIndirectKill(killer_pokemon_team, killer_turn.split('p' + killer_pokemon_team +
					                                                              'a: ')[-1].split('|')[0])

			# Check for an indirect kill based on Ability or Rocky Helmet
			elif ('ability:' in passive_reason or passive_reason == 'item: Rocky Helmet'):
				self.__addIndirectKill(killer_pokemon_team,
				                       log_copy.split(fainted_pokemon + '|0 fnt|[from] ', 1)[-1].split(
					                       '[of] p' + killer_pokemon_team + 'a: ')[1].split('\n')[0])

			# Check for an indirect kill based on Entry Hazards
			elif (passive_reason == 'Stealth Rock' or passive_reason == 'Spikes'):
				self.__addIndirectKill(killer_pokemon_team, self.__getHazardSetter(killer_pokemon_team, passive_reason))

			# Check for an indirect kill based on moves that damage over time
			elif ('move' in passive_reason):
				move = log_copy.split(fainted_pokemon + '|0 fnt|[from] move: ', 1)[-1].split('|')[0]
				self.__addIndirectKill(killer_pokemon_team,
				                       log_copy.split(fainted_pokemon + '|0 fnt|[from] move: ', 1)[-2].split(
					                       '|' + move)[-2].split('|p' + killer_pokemon_team + 'a: ')[1].split('|')[0])

			elif (passive_reason == 'Sandstorm' or passive_reason == 'Hail'):
				if (killer_pokemon_team ==
						log_copy.split('|' + passive_reason + '|[from]')[-2].split('|p')[-1].split('a: ')[0]):
					self.__addIndirectKill(killer_pokemon_team,
					                       log_copy.split('|' + passive_reason + '|[from]')[-2].split('|p')[-1].split(
						                       '|')[0].split('a: ')[1])

			elif (passive_reason == 'Leech Seed'):
				self.__addIndirectKill(killer_pokemon_team,
				                       re.findall(r'p' + killer_pokemon_team + 'a: (.*?)\|Leech Seed\|', log_copy)[-1])

			log_copy = log_copy.split('0 fnt|[', 1)[1]

	def __getHazardSetter(self, team, hazard):
		return self.__log.rsplit('|' + hazard, 1)[-2].split('p' + team + 'a: ')[-1].split('|')[0]

	def __addIndirectKill(self, team, nickname):
		self.__teams[team].getPokemonWithNickname(nickname).indirect_kills += 1