from matchmaking import *

class Tournament:
    pass

class GroupStage(Tournament):
    pass

class Playoffs(Tournament):
    pass

class Continous(Tournament):
    def __init__(self, match_maker, stage_limit=-1):
        self.stages = []
        self.stage_limit = stage_limit
        self.match_maker = match_maker
        self.stage_limit = stage_limit
        
    def run(self, players):
        for stage in range(self.stage_limit):
            matches = self.match_maker.find(players, state=stage)
            print(matches)

class Game:
    def __init__(self, tournamnet, players=None):
        self.tournament = tournamnet
        self.players = players or []
    
    def add_player(self, player):
        self.players.append(player)
    
    def load_players(self, file):
        pass
    
    def print_ranks(self):
        # TODO: this can be generalized into a "print_table(columns)" function
        name_size = max([len(i.name) for i in self.players])
        num_size = max([len(str(i.rank.linear)) for i in self.players])
        
        print("-" * (name_size + num_size + 5))
        for p in self.players:
            print("|", p.name.ljust(name_size), str(p.rank.linear).rjust(num_size), "|")
        print("-" * (name_size + num_size + 5))
    
    def run(self):
        self.print_ranks()
        self.tournament.run(self.players)
        