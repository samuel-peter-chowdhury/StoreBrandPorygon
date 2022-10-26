import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

from Match import Match

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_NAME = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='Porygon, use ', intents=intents)

@bot.event
async def on_ready():
	GUILD_OBJECT = discord.utils.get(bot.guilds, name=GUILD_NAME)
	print(f'{bot.user} is connected to the following guild:\n{GUILD_OBJECT.name}(id: 'f'{GUILD_OBJECT.id})')

@bot.event
async def on_message(message):
	if message.channel.name == 'live-links' and 'https://replay.pokemonshowdown.com' in message.content:
		match = Match(message.content + '.json')
		match.parseData()
		response = match.toString()
		if match.strangeResults():
			response += '\n<@' + str(message.author.id) + '>, the kills and deaths don\'t line up...Investigate please.'
		await message.channel.send(response)

@bot.command(name='analyze', help='Use this command followed a league replay url.')
async def analyze(ctx, replay):
	match = Match(replay + '.json')
	match.parseData()
	await ctx.channel.send(match.toString())
	return