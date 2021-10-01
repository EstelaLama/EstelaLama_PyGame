# -*- coding: utf-8 -*-
"""
Sun Feb  7 
Human Behavior Prediction
@author: Estela lama
"""
def game(): 
    #assigning variables
    computer_move, player_move, select_difficulty, restart, moves = 0, 0, 0, 0, 1
    computer_score, player_score, total_computer_score, total_player_score = 0, 0, 0, 0
    throw00=0 #count of human player chose 0 given that the previous bid was 0
    throw01=0 #count of human player chose 0 given that the previous bid was 1
    throw10=0 #count of human player chose 1 given that the previous bid was 0
    throw11=0 #count of human player chose 1 given that the previous bid was 1
    player_moves = []
    yes_list = ["yes", "y", "Y", "Yes"]
    xi = 1234
    
    #Function to calculate linear congruence values and computer's easy bet
    def linear_congruence(xi):
        xi_plus_1 = (22695477 * xi + 1) % (2**32)
        if xi_plus_1 <= 2**31: 
            computer_move = 0
        else: 
            computer_move = 1
        return computer_move, xi_plus_1
    
    #defining function so the computer can "predict" human's throw by his previous bid
    def computer_difficult_move(): 
        xi=1234
        if (player_move == 0 and throw10 > throw00) or (player_move == 1 and throw11 > throw01):
            computer_move = 1
        elif (player_move == 0 and throw10 < throw00) or (player_move == 1 and throw11 < throw01):
            computer_move = 0
        else:
            computer_move,xi = linear_congruence(xi)
        return (computer_move)

    #printing the score after every round
    def print_score(): 
        print("You: ", player_score, "computer: ", computer_score)
        print("PLAYER: ", "*" * player_score)
        print("COMPUTER: ", "*" * computer_score)
    
    #Opening Message
    print("\nWelcome to the Human Behavior Prediction by Estela Lama! \n\nThe game consists of, you, a human player and the computer. Both choose either the value 0 or the value 1. If both choose the same numbers, the computer earns a point. If the numbers chosen are different, the human player earns a point. You keep playing as many rounds as you want.")
    
    #selecting game difficulty
    while True: 
        try: 
            select_difficulty  = int(input("\nPlease choose the type of game (1: Easy; 2: Difficult): "))
            if select_difficulty == 2:
                break
            elif select_difficulty == 1:
                break
            else:
                print("Please slect 1: Easy or 2: Difficult")
        except:
            print("Please choose 1 or 2")
    
    #Choose how many rounds will be played
    while True: 
        try: 
            moves = int(input("\nEnter the number of moves: "))
            if moves > 0: 
                break
            else: print("Please select an integer greater than 1, so we can start playing.")
        except: print("Please select how many times you will like to play, it could be 1 or more rounds.")
    
    #Start of the game, player chooses it's throw
    for turn in range (moves): 
        while True: 
            try: 
                player_move = int(input("\nChoose your move for round: %s (0 or 1): " % (turn+1)))
                if (player_move == 1) or (player_move == 0):
                    player_moves.append(player_move) #adding move to list
                    break
                else: print("Please choose 1 or 0")
            except: print("Please choose either 0 or 1 to play")
            # adding player movesto throws
            throw00= sum(player_moves[turn]==0 and player_moves[turn-1]==0)
            throw01= sum(player_moves[turn]==0 and player_moves[turn-1]==1) 
            throw10= sum(player_moves[turn]==1 and player_moves[turn-1]==0) 
            throw11= sum(player_moves[turn]==1 and player_moves[turn-1]==1)        
        #computer chooses easy or difficult move    
        if select_difficulty == 1: #if game is easy
            computer_move, xi = linear_congruence(xi)
        else: computer_move = computer_difficult_move() #else play difficult mode
        
        #print score after every move
        if player_move == computer_move: 
            computer_score = computer_score + 1
            print("Player Move=", player_move, " Machine Move=", computer_move, ". Machine wins!")
        elif player_move != computer_move:
            player_score = player_score + 1
            print("Player Move=", player_move, " Machine Move=", computer_move, ". Player wins!")
        print_score()
    
    #Printing who is the winner of the game or if there's a tie
    if select_difficulty == 1: #Show final score for easy game
        if player_score > computer_score:
            total_player_score = total_player_score + 1
            print("\nYou Won! \nEasy Game is Over final result Player:", player_score, " - Computer:", computer_score)
        elif player_score < computer_score:
            total_computer_score = total_computer_score + 1
            print("\nComputer Won! \nEasy Game is Over final result Player:", player_score, " - Computer:", computer_score)
        else: print("\nIt was a tie! Try again if you want too!")
    if select_difficulty == 2: #Show final score for difficult game
        if player_score > computer_score:
            total_player_score = total_player_score + 1
            print("\nYou Won! \nDifficult Game is Over final result Player:", player_score, " - Computer:", computer_score)
        elif player_score < computer_score:
            total_computer_score = total_computer_score + 1 
            print("\nComputer Won! \nDifficult Game is Over final result Player:", player_score, " - Computer:", computer_score)
        else: print("\nIt was a tie! \nPlay against the computer and see if you are able to beat it!")
    
    #Prompt to restart game    
    print("\nTotal Player Wins:", + total_player_score, "\nTotal Computer Wins:", + total_computer_score)
    restart = input("\nDo you want to start a new game? Yes (Y) or No (N):")
    if restart in yes_list:
        game()
    else: exit()

game() #initiating the game