"""
Name of the project: Python Individual Assignment
Description: Human behaviour game
Author: Michelle Michalowski
Last Updated: 07/02/2021
"""
#import linear congurence package 
from mypackage.demo import linear_congruence

#define start seed
xi=1234

#initialize difficulty
difficulty=0

#define computer decision function 
def my_robo(computer_move):
    #only if we play in diificult mode and we have stored more than 2 values
    if difficulty == 2 and len(move_history) >= 2:
        if move_history[-1] == 0:
            if throw_10 > throw_00:
                return 1
            if throw_10 < throw_00:
                return 0
            else: return computer_move 
        if move_history[-1] == 1:  
            if throw_11 > throw_01:
                return 1
            if throw_11 < throw_01:
                return 0
            else: return computer_move 
    else: return(computer_move)
                                 
#define function to allow user only to answer correct                         
def check_input(message,valid_options):
   while True:
       value = input(message)
       if value not in valid_options or value.strip() == '':
           print("Please enter valid answer!")
       else: 
           return value
   
print("Welcome to Human Behavior Prediction by Michelle Michalowski")

#define counter for number of game wins
player_wins, computer_wins = 0, 0 

#initialize the history of player moves as list
move_history = []   

#define counters for player throws
throw_10, throw_00, throw_11, throw_01 = 0,0,0,0       
            
while True: 
    #initialize points counters 
    MS,PS = 0, 0      
            
    #define variables difficulty and moves
    difficulty = int(check_input("Please choose the type of game (1: Easy, 2: Difficult): ", ("1","2")))
    moves = int(check_input("Enter number of moves: ", str(list(range(1,51)))))
    
    #THE GAME
    for turn in range(1, moves + 1):
        computer_move, xi = linear_congruence(xi)
        computer_move = my_robo(computer_move)
        #ask for player move
        player_move = int(check_input("ROUND " + str(turn) + " Choose your move for round: " + str(turn) + " (0 or 1): ", ("0","1")))
        move_history.append(player_move)
        if len(move_history) >= 2:
            #define counter for the throws, get the last two moves with move history list
            if  move_history[-1] == 1 and move_history[-2] == 0:
                throw_10 = throw_10 + 1 
            elif move_history[-1] == 1 and move_history[-2] == 1:
                throw_11 = throw_11 + 1
            elif move_history[-1] == 0 and move_history[-2] == 1:
                throw_01 = throw_01 + 1
            elif move_history[-1] == 0 and move_history[-2] == 0:
                throw_00 = throw_00 + 1
        if player_move == computer_move: 
            #counter for machine wins
            MS = MS + 1
            print("Player Move =", player_move, " Machine Move =",computer_move," .Machine wins!" )
            print("You: %d Computer %d" % (PS, MS))
        else:
            #counter for player wins
            PS = PS + 1
            print("Player Move =", player_move, " Machine Move =",computer_move," .Player wins!" )
            print("You: %d Computer %d" % (PS, MS))       
        print('PLAYER: ' + '*' *PS) 
        print('COMPUTER: ' + '*' *MS)
     
    #counter for how often machine/player wins    
    if PS > MS:
        player_wins = player_wins + 1
    elif MS > PS:
        computer_wins = computer_wins + 1
    else: 
        print('Game was tied')
    #do you want to play again?  
    play_again = check_input("Do you want to start a new game? Yes (Y) No (N):", ("y", "Y", "n", "N"))
    if play_again.lower()=="y":
        continue
    else:
        print("Total Player Wins: " + str(player_wins) + "\n"
              "Total Computer Wins: " + str(computer_wins))
        break
