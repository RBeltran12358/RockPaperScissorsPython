import random

# 2/3   3/5  4/5
def main():
    # declaring and initializing some variables
    up_to = int(input("How many points do you want to play to? "))
    comp_scr = 0
    while up_to < 1:
        up_to = int(input("Invalid Number of Games. How many points do you want to play to? "))
    player_scr = 0

    comp_options = ["rock", "paper", "scissor"]
    comp = comp_options[random.randrange(0, 3, 1)]
    play_again = True
    print(False and True and True)
    # print(type(i))
    while play_again and comp_scr < up_to and player_scr < up_to:
        i = input("rock, paper, or scissor? ")
        while i != "rock" and i != "Rock" and i != "paper" and i != "Paper" and i != "Scissor" and i != "scissor":
            i = input("Wrong Input, try again. rock, paper, scissor? ")

        if i == "rock" or i == "Rock":
            if comp == "rock":
                print("Tie! Choose again:) ")
            elif comp == "paper":
                player_scr += 1
                if player_scr != up_to:
                    print("Horray! You've won, " + str((up_to - player_scr)) + " more points to go!")
            else:
                comp_scr += 1
                if comp_scr != up_to:
                    print("Close! the computer won this round. Don't let it get " + str(
                        (up_to - comp_scr)) + " more points! ")
        elif i == "paper" or i == "Paper":
            if comp == "paper":
                print("Tie! Choose again:) ")
            elif comp == "rock":
                player_scr += 1
                if player_scr != up_to:
                    print("Horray! You've won, " + str((up_to - player_scr)) + " more points to go!")
            else:
                comp_scr += 1
                if comp_scr != up_to:
                    print("Close! the computer won this round. Don't let it get " + str(
                        (up_to - comp_scr)) + " more points! ")
        else:
            if comp == "scissor":
                print("Tie! Choose again:) ")
            elif comp == "paper":
                player_scr += 1
                if player_scr != up_to:
                    print("Horray! You've won, " + str((up_to - player_scr)) + " more points to go!")
            else:
                comp_scr += 1
                if comp_scr != up_to:
                    print("Close! the computer won this round. Don't let it get " + str(
                        (up_to - comp_scr)) + " more points! ")

        if comp_scr == up_to:
            print("Oops! The computer seems to have won this one!")
            again = input("Do you want to play again? y for yes , n for no ")
            if again == "n":
                play_again = False
                #i = None
            if again == "y":
                comp_scr = 0
                player_scr = 0
        elif player_scr == up_to:
            print("Yay you beat the computer!")
            again = input("Do you want to play again? y for yes , n for no ")
            if again == "n":
                play_again = False
                #i = None
            if again == "y":
                comp_scr = 0
                player_scr = 0
    print("Thank you for playing!")


    """
            if comp_scr == up_to:
        print("Oops! The computer seems to have won this one!")
        again = input("Do you want to play again? y for yes , n for no ")
        if again == "n":
            play_again = False
            i = None
        if again == "y":
            comp_scr = 0
            player_scr = 0
        
    elif player_scr == up_to:
        print("Yay you beat the computer!")
        again = input("Do you want to play again? y for yes , n for no ")
        if again == "n":
            play_again = False
            i = None
        if again == "y":
            comp_scr = 0
            player_scr = 0
            
            
            
                    else:
        i = input("rock, paper or scissor? ")
        comp = comp_options[random.randrange(0, 3, 1)]
    """


if __name__ == "__main__":
    main()

