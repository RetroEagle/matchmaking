from tournament import *
from matchmaking import *

g = Game(Continous(), players=[Player("Daniel", Rank(linear=100)),
                               Player("Malte", Rank(linear=-1)),
                               Player("Erica", Rank(linear=0.5)),
                               Player("Rutger"),
                               Player("Lien"),
                               Player("Philipp"),
                               Player("God"),
                               Player("John Wick")])

g.run()