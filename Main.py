from Match import Match

if __name__ == '__main__':
    match = Match('https://replay.pokemonshowdown.com/sports-gen8nationaldexlegacy-742172.json')
    match.parseData()
    print(match.toString())