import random

player_win_count = 1
computer_win_count = 1
display_game_choice = """
Choose 1 for scissors
Choose 2 for paper
Choose 3 for rock
"""
print(display_game_choice)
count = 0


computer_pick = random.randint(0, 2)
while count != 5:
    player_pick = int(input("Enter number to select "))
    computer_pick = random.randint(0, 2)
    if computer_pick == 0:
        print("computer picked: scissors")
    elif computer_pick == 1:
        print("computer picked: paper")
    else:
        print("computer picked: rock")
    match computer_pick:
        case 0:
            if player_pick == 3:
                print("player wins")
            elif player_pick == 2:
                print("computer wins")
            else:
                print("Tie game")
        case 1:
            if player_pick == 3:
                print("computer wins")
            elif player_pick == 2:
                print("player wins")
            else:
                print("Tie game")
        case 2:
            if player_pick == 3:
                print("Tie game")
            elif player_pick == 2:
                print("player wins")
            else:
                print("computer wins")
    count = count + 1
    display_game_choice = """
Choose 1 for scissors
Choose 2 for paper
Choose 3 for rock
"""
    print(display_game_choice)

