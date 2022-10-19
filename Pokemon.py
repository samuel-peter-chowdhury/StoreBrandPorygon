class Pokemon():
    def __init__(self, name):
        self.name = name
        self.nickname = ''
        self.direct_kills = 0
        self.indirect_kills = 0
        self.dead = False
        self.mega_name = ''

    def __str__(self):
        return '{} has {} direct kills, {} passive kills, and {} deaths.'\
            .format(self.name if self.mega_name == '' else self.mega_name, self.direct_kills, self.indirect_kills, '1' if self.dead else '0')