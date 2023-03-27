from art import logo, vs
from replit import clear
import random
from game_data import data

def run_logo():
    """Clear the screen and print logo"""
    clear()
    print(logo)


def rerun():
    """ Helps end the loop if the user wants to stop it"""
    restart = input("Do you want to continue. Type 'y' and 'n' to end: ")
    if restart == 'n':
        game_rerun = False
        return game_rerun
    else:
        game_rerun = True
        return game_rerun
        
def game(): 
    def user_pick():
        """ Matches user input to the follower count"""
        if USER_CHOICE == 'A':
            user_option = FOLLOWER_A 
            return user_option
        elif USER_CHOICE == 'B':
            user_option = FOLLOWER_B
            return user_option

    run_logo()
    user_name = input("What's your name: ")
    game_play = True
    score = 0
    while game_play is True:
        run_logo()
        
        choice_1 = random.choice(data)
        choice_2 = random.choice(data)
        
        FOLLOWER_A = choice_1['follower_count']
        FOLLOWER_B = choice_2['follower_count']
        
        print(f"Compare A: {choice_1['name']}, a {choice_1['description']}, from {choice_1['country']}\n{vs}\nCompare B: {choice_2['name']}, a {choice_2['description']}, from {choice_2['country']} ")
        
        USER_CHOICE = input("Who has more followers? Type 'A' or 'B': ").upper()
        
        if user_pick() == FOLLOWER_A and user_pick() > FOLLOWER_B:
            score += 1
            run_logo()
            print(f"You're right! Current Score: {score}")
            game_play = rerun()
        elif user_pick() == FOLLOWER_B and user_pick():
            score += 1
            run_logo()
            print(f"You're right! Current Score: {score}")
            game_play = rerun()
             
        else:
            game_play = False
            run_logo()
            print(f"Sorry {user_name}, that's wrong, Final score: {score}")
    
    
    
    restart_game = input("Do you want to Play again. Type 'y' and 'n' to stop: ")
    if restart_game == 'y':
        game()
    else:
        run_logo()
        print(f"Goodbye, {user_name}")


game()
    
