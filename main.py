#Rock-Paper-Scissors

# Import random module
import random

# Function: Play
def Play():
    # user input
    user = ''
    while user != 'r' and user != 'p' and user != 's':
        user = input("Let's play Rock-Paper-Scissors Game!\n'r' for Rock, 'p' for Paper, 's' for Scissors: ").lower()

    com = random.choice(['r', 'p', 's']) # random for computer
    text = {"r":"Rock", "p": "Paper", "s":"Scissors"}

    # tie
    if user == com:
        return f'User: {text[user]}\nCom: {text[com]}\nTie! Try one more!'

    # user win
    if (user=='r' and com=='s') or (user=='p' and com=='r') or (user=='s' and com=='p'):
        return f'User: {text[user]}\nCom: {text[com]}\nYou win!'

    # user lose
    return f'User: {text[user]}\nCom: {text[com]}\nYou lose.'

# Run function
print(Play())