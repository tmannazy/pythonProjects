import random

if __name__ == '__main__':
    magic_number = random.randint(1, 100)
    counter = 0

    while counter < 3:
        userResponse = int(input("Guess a number between 0 and 100: "))
        if userResponse < 0 or userResponse > 100:
            print("You are really daft...See ya!")
            break
        elif userResponse < magic_number:
            print("Your guess is low. Try again!")
        elif userResponse > magic_number:
            print("Your guess is too high. Try again!")
        else:
            print("Correct! You got it...")
            break
        counter += 1
    else:
        print("You have exceeded your trials. Good bye...")
        print("The correct number is: ", magic_number)
