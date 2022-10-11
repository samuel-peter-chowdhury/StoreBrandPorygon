from Match import Match

if __name__ == '__main__':
    match = Match('https://replay.pokemonshowdown.com/gen8nationaldexag-1680375495-nazywfcmf2ntlfegv6544qyjkf6qhtgpw.json')
    match.parseData()
    print(match.toString())