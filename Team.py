class Team():
    def __init__(self):
        self.coach = ''
        self.pokemon = {}
        self.nickname_map = {}

    def getPokemonWithNickname(self, nickname):
        return self.pokemon[self.nickname_map[nickname]]