import random as r 


def roll_dice():
    return r.randint(1,6)

def play_game():
    roll1 = roll_dice()
    roll2 = roll_dice()
    total = roll1 + roll2 
    print(f'The sum of dice is {roll1} + {roll2} = {total}')
    if total in [7, 11]:
        print('You won!')
    elif total in [2, 3, 12]:
        print('You lose')
    else:
        goal = total
        print(f'Now your goal number is {goal}')
        while True:
            roll1 = roll_dice()
            roll2 = roll_dice()
            total = roll1 + roll2 
            print(f'The sum of dice is {roll1} + {roll2} = {total}')
            if total == goal:
                print('You won!')
                break
            elif total == 7:
                print('You lose')
                break
play_game()
