#threecardmonte.py

from graphics import GraphWin, Point
from button import Button
from random import randrange

#wont let me import doors, need admin access

class Door:
	"""a door is a rectangle in a window.
	It is activated or deactivated with the activate()
	and deactivate() methods. The door remains inactive (peach) until
	the user makes a correct guess, and wins (green)."""
	
	def __init__(self, win, center, width, height):
		"""Creates a rectangle that changes color depending on a
        correct guess by the user eg:
		door1 = Door(myWin, centerPoint, width, height)"""
		
		w, h = width/2.0, height/2.0
		x, y = center.getX(), center.getY()
		self.xmax, self.xmin = x+w, x-w
		self.ymax, self.ymin = y+h, y-h
		p1 = Point(self.xmin, self.ymin)
		p2 = Point(self.xmax, self.ymax)
		self.rect = Rectangle(p1, p2)
		self.rect.setFill("peachpuff")
		self.rect.draw(win)
		self.deactivate()
		
	
	def activate(self):
		"Sets this button to 'active'."
		self.rect.setFill("green2")
		self.rect.setWidth(1)
		self.active = True
		
	def deactivate(self):
		"Sets this button to 'inactive'."
		self.rect.setFill("peachpuff")
		self.rect.setWidth(1)
		self.active = False

def main():

    #Create the game view window
    win = GraphWin("GameView", 700, 500)
    #win.setCoords(0, 0, 10, 10)
    win.setBackground("lightblue")
    
	#makes rectangles that represent doors.
	door1 = Door(win, Point(175, 150), 90, 130)
	door1.deactivate()
	door2 = Door(win, Point(350, 150), 90, 130)
	door2.deactivate()
	door3 = Door(win, Point(525, 150), 90, 130)
	door3.deactivate()

    winCount = 0
    loseCount = 0
    correct = randrange(1,4)
    choice = 0

    # draw the buttons
    cb1 = Button(win, Point(175,350), 130, 45, "Option 1")
	cb1.activate()
	cb2 = Button(win, Point(350,350), 130, 45, "Option 2")
	cb2.activate()
	cb3 = Button(win, Point(525,350), 130, 45, "Option 3")
	cb3.activate()
	qb = Button(win, Point(350,450), 150, 45, "Quit")

    pt = win.getMouse()
    
    while not qb.clicked(pt):
        
        if cb1.clicked(pt):
            choice = 1
        elif cb2.clicked(pt):
            choice = 2
        elif cb3.clicked(pt):
            choice = 3

        if choice == correct:
            winCount = winCount + 1
            print("you win, keep going or quit")
        else:
            loseCount = loseCount + 1
            print("you lose, keep going or quit")

        qb.activate()
        pt = win.getMouse()
        
    wMessage = str(winCount)
    lMessage = str(loseCount)
    print("you won "+wMessage+" times.")
    print("you lost "+lMessage+" times.")
    win.close()

main()
