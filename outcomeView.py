# dieview.py
from graphics import *
class OutcomeView:
    """ DieView is a widget that displays a graphical representation
    of a standard six-sided die."""
    
    def __init__(self, win, center, size):
        """Create a view of a die, e.g.:
           d1 = GDie(myWin, Point(40,50), 20)
        creates a die centered at (40,50) having sides
        of length 20."""

        # first define some standard values
        self.win = win            
        self.background = "peachpuff" 
        self.correct = "green"
        self.wrong = "red"
        cx, cy = center.getX(), center.getY()
        self.csize = size / 2.0   
        lsize = size / 2.0              

        # Create the correct or wrong symbols for the outcome of the game
        self.correct1 = self.__makeCorrect(cx, cy)
        self.wrong1 = self.__makeWrong(cx-lsize, cx+lsize, cy+lsize, cy-lsize)
        self.wrong2 = self.__makeWrong(cx+lsize, cx-lsize, cy+lsize, cy-lsize)
        

    def __makeCorrect(self, x, y):
        "Internal helper method to draw a pip at (x,y)"
        correctOutcome = Circle(Point(x,y), self.csize)
        correctOutcome.setFill(self.background)
        correctOutcome.setOutline(self.background)
        correctOutcome.draw(self.win)
        return correctOutcome

    def __makeWrong(self, x1, x2, y1, y2):
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        wrongOutcome = Line(p1,p2)
        wrongOutcome.draw(self.win)
        wrongOutcome.setFill(self.background)
        return wrongOutcome

    def setOutcome(self, value):
        "Set this die to display value."
        # turn all pips off
        self.correct1.setFill(self.background)
        self.wrong1.setFill(self.background)
        self.wrong2.setFill(self.background)

        # turn correct pips on
        if value == 1:
            self.correct1.setFill(self.correct)
        elif value == 2:
            self.wrong1.setFill(self.wrong)
            self.wrong2.setFill(self.wrong)
        else:
            self.correct1.setFill(self.background)
            self.wrong1.setFill(self.background)
            self.wrong2.setFill(self.background)
