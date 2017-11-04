# Craig Hurely
# 2017/11/02
#threecardmonte.py

from graphics import GraphWin, Point
from button import Button
from random import randrange
from outcomeView import OutcomeView

def main():

    #Create the game view window
    win = GraphWin("GameView", 700, 500)
    win.setBackground("lightblue")

    # creates three variables and starts them at zero.
    winCount = 0
    loseCount = 0
    choice = 0

    # draws the cards (buttons) and activates them.
    # card 1
    cb1 = Button(win, Point(175,175), 150, 250, "Option 1")
    cb1.activate()
    # card 2
    cb2 = Button(win, Point(350,175), 150, 250, "Option 2")
    cb2.activate()
    # card 3
    cb3 = Button(win, Point(525,175), 150, 250, "Option 3")
    cb3.activate()
    
    # Quit Button
    qb = Button(win, Point(350,450), 130, 45, "Quit")
    
    # Draws the visual representation of a correct choice or a wrong choice
    # The outcome is assigned to their respective cards
    outcome1 = OutcomeView(win, Point(175,175), 140)
    # Draws outcome 2
    outcome2 = OutcomeView(win, Point(350, 175), 140)
    # Draws outcome 3
    outcome3 = OutcomeView(win, Point(525, 175), 140)
    
    

    # Creates a start point for the sentinel loop.
    correct = randrange(1,4)
    pt = win.getMouse()

    # Continues as long as the quit button isn't pressed.
    while not qb.clicked(pt):

        # Event for Button 1
        if cb1.clicked(pt):
            choice = 1
            # Event for a correct choice
            if choice == correct:
                winCount = winCount + 1
                outcome1.setOutcome(1)
                print("you win, keep going or quit")
            else:
                loseCount = loseCount + 1
                outcome1.setOutcome(2)
                print("you lose, keep going or quit")
        # Event for Button 2
        elif cb2.clicked(pt):
            choice = 2
            # Second correct event
            if choice == correct:
                winCount = winCount + 1
                outcome2.setOutcome(1)
                print("you win, keep going or quit")
            else:
                loseCount = loseCount + 1
                outcome2.setOutcome(2)
                print("you lose, keep going or quit")
        # Event for Button 3
        elif cb3.clicked(pt):
            choice = 3
            # Third correct event
            if choice == correct:
                winCount = winCount + 1
                outcome3.setOutcome(1)
                print("you win, keep going or quit")
            else:
                loseCount = loseCount + 1
                outcome3.setOutcome(2)
                print("you lose, keep going or quit")
                
        # Resets loop
        qb.activate()
        pt = win.getMouse()
        correct = randrange(1,4)
        outcome1.setOutcome(0)
        outcome2.setOutcome(0)
        outcome3.setOutcome(0)
        

    # Converts win and lose count to strings.
    wMessage = str(winCount)
    lMessage = str(loseCount)

    # Prints a message displaying wins and loses. 
    print("you won "+wMessage+" times.")
    print("you lost "+lMessage+" times.")
    win.close()

main()
