## CTS 285
## Dungeon Fighters
## Reginald Jones
## Nov 2nd, 2021
##

##Game Project for CTS 285 Class


"""
A Basic Dungeon Crawler
"""

#Start Point: Character Name and Class Creation

print("\nHello,")
print("\nEnter Your Name")

#User Chooses which Adventure Field to Start
##TODO


#Treasure Chest Unlock
##TODO

##Combat
##Used as reference for basic combat. Rock Paper Scissors Format

##TODO


##Import Functions
#import reginald_jones_game_functions as game
#import random
#
## Global constants
#COMPUTER_WINS = 1
#PLAYER_WINS = 2
#TIE = 0
#INVALID = 3
#ROCK = 1
#PAPER = 2
#SCISSORS = 3
#
##Welcome Message
#def welcome_message():
#    print("\nThis is A Game of Choice.")
#    print("Good Luck")
#
##Function to Run The Game, named ChoiceGame    
#def choicegame():
#    
#    result = TIE
#
#    while result==TIE:
#        # Get computer number, determined by random function
#        computer = random.randint(1, 3)
#
#        # Get player number input
#        player = int(input('Enter "1" for Rock, ' \
#                           '"2" for Paper or "3" for Scissors: '))
#
#        print ('Computer chose', game.choiceString(computer))
#        print ('You chose', game.choiceString(player))
#        
#        result = game.rockPaperScissors(computer, player)
#        
#        #If game results in a tie
#        if result == TIE:
#            print('You made the same choice as ' \
#                  'the Computer. Starting over')
#    
#    #If the Computer wins
#    if (result == COMPUTER_WINS):
#        print ('The Computer wins the game')
#    
#    #If the Player Wins    
#    elif result == PLAYER_WINS:
#        print ('You win the game')
#    
#    #If an invalid number is entered.        
#    else:
#        print ('You made an invalid choice. No winner')
#
##Main function that starts at the beginning of the program
##Uses a while loop to determine if User will continue the game
#def main():
#    welcome_message()
#    again = "y"
#    while again.lower() == "y":
#        #If y is chosen the game will restart
#        choicegame()
#        print()
#        again = input("Would You Like To Play Again? (y/n):  ")
#        print()
#    #End Message if n is chosen
#    print("Program Will End. Goodbye.")
#    
## Call the main function.
#if __name__ == "__main__":
#    main()