import random

class Rank:
    """
    additive:
        adds the score to the rank
    
    linear:
        adds score difference to rank
        
    """
    def __init__(self, additive=0, linear=0):
        # TODO: maybe use dict here
        
        self.additive = additive
        self.linear = linear

class Player:
    def __init__(self, name, rank=None):
        self.name = name
        self.rank = rank or Rank()
        
    def __lt__(self, other):
        return self.name < other.name
    
    def __repr__(self) -> str:
        return self.name
        
class Match:
    def __init__(self, teams: tuple[tuple[Player, ...], ...]):
        self.teams = teams
        
    def __print__(self):
        cutoff = 2 if len(self.teams[0]) == 1 else 1    
        printStr = "|" + str(self.teams[0])[1:-cutoff]
        for team in self.teams[1:]:
            printStr += " vs " + str(team)[1:-cutoff]
        
        return printStr + "|"
            
    def __repr__(self):
        return self.__print__()
            
class MatchMaker:
    """
    replacement:
        if true, once a player has been draw, they cannot player with or against the same constellation again
        (maybe implement this somewhere else... not ideal to also store past matches here)
        
    weighted:
        if true, will use the score of the game for rank calculation. If false, will use 0 for looser and 1 for winner
        
    biased:
        if true, will use the original rank of the players for rank calculationd
        
    dynamic:
        if ture, allows fair matchup with teams below team size.
        
    team_tize:
        size of each team
        
    opponenets:
        amount of teams that play in one match
      
    """
    def __init__(self, replacement=True, weighted=True, biased=True, dynamic=True, team_size=1, opponents=2):
        # self.players = players
        # self.matches = matches
        
        self.replacement = replacement
        self.weighted = weighted
        self.biased = biased
        self.dynamic = dynamic
        self.team_size = team_size
        self.opponents = opponents
        
    def find(self, players, state=0, restrictions=None):
        """
        out:
            list of matches: [Match]
        """
        seed = random.Random(str([p.name for p in players]) + str(state)).getrandbits(48)
        
        restrictions = restrictions or []
        # TODO: resolve this mess
        # neat implementation: DFS (Backtracking) to avoid any livelocks. AC3 would be faster but total overkill
        # for now, just ignore restrictions
        restrictions = [sorted([sorted(team) for team in match]) for match in restrictions]
        
        temp_players = list(players)
                
        # find teammates
        teams = []
        while len(temp_players) > 0:
            team = ()
            while len(team) < self.team_size:
                # seed = seed * 3 + 1
                seed = random.Random(str(seed)).getrandbits(48)
                team += (temp_players.pop(seed % len(temp_players)),)
            teams.append(team)
        
        
        # find opponets
        matches = []
        while len(teams) > 0:
            _match = ()
            while len(_match) < self.opponents:
                seed = random.Random(str(seed)).getrandbits(48)
                _match += (teams.pop(seed % len(teams)),)
            matches.append(Match(_match))
            
        return matches
