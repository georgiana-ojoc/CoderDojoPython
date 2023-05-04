"""
Rock, Paper, Scissors
"""

import random
import re


def get_user_choice():
    user_choice = input("Choose your weapon [R]ock], [P]aper, or [S]cissors: ")
    letters_regex = "[SsRrPp]"
    # Check if user's input is correct
    if not re.match(letters_regex, user_choice):
        while True:
            user_choice = input("Please choose a letter ([R]ock], [P]aper, or [S]cissors): ")
            if re.match(letters_regex, user_choice):
                break
    return user_choice


def main():
    while True:
        print("\nRock, Paper, Scissors - Shoot!")
        user_choice = get_user_choice()
        print("You chose: " + user_choice)
        choices = ['R', 'P', 'S']
        computer_choice = random.choice(choices)
        print("I chose: " + computer_choice)
        if computer_choice == str.upper(user_choice):
            print("Tie!")
        elif computer_choice == 'R' and user_choice.upper() == 'S':
            print("Scissors beats rock, I win!")
        elif computer_choice == 'S' and user_choice.upper() == 'P':
            print("Scissors beats paper, I win!")
        elif computer_choice == 'P' and user_choice.upper() == 'R':
            print("Paper beats rock, I win!")
        else:
            print("You win!")


if __name__ == '__main__':
    main()
