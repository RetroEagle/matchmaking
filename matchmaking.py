class Rank:
    """
    additive:
        adds the score to the rank
    
    linear:
        adds score difference to rank
        
    """
    def __init__(self, additive=0, diff=0):
        self.additive = additive
        self.linear = linear

class Player:
    def __init__(self, name):
        self.name = name
        
class Match:
    def __init__(self, teams: tuple[tuple[Player, ...], ...]):
        pass

class MatchMaker:
    """
    replacement:
        if true, once a player has been draw, they cannot player with or against the same constellation again
        
    weighted:
        if true, will use the score of the game for rank calculation. If false, will use 0 for looser and 1 for winner
        
    biased:
        if true, will use the original rank of the players for rank calculationd
    """
    def __init__(self, players, matches, replacement=True, weighted=True, biased=True):
        self.players = players
        self.matches = matches
        
        self.replacement = replacement
        self.weighted = weighted
        self.biased = biased