from Match import Match

if __name__ == '__main__':
    match = Match('https://replay.pokemonshowdown.com/gen8nationaldexag-1680380125-qmzyer5siqimo3xntb5ec9v82e5gugjpw.json')
    match.parseData()
    print(match.toString())