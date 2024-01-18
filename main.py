from tournament import *
from matchmaking import *

# g = Game(Continous(), players=[Player("Daniel", Rank(linear=100)),
#                                Player("Malte", Rank(linear=-1)),
#                                Player("Erica", Rank(linear=0.5)),
#                                Player("Rutger"),
#                                Player("Lien"),
#                                Player("Philipp"),
#                                Player("God"),
#                                Player("John Wick")])

g = Game(Continous(MatchMaker(team_size=2), 4), 
        players=[Player("A", Rank(linear=100)),
                Player("C", Rank(linear=0.5)),
                Player("B", Rank(linear=-1)),
                Player("D"),
                Player("E"),
                Player("F"),
                Player("G"),
                Player("H")])


g.run()