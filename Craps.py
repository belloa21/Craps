#Alex Bello
#10/23/2019

import random


def roll_dice():
    roll = random.randint(2, 12)
    return roll


def create():
    print("How much money is in your starting bankroll?")
    return int(input())


def play_again():
    print('Would you like to play again? (Y) or (N).')
    result = input()
    if 'y' in result:
        return True
    else:
        return False


def play_game():
    bankroll = create()
    bet = 0
    play = True
    while play and bankroll:
        print(f"How much ya wanna put up from ${bankroll} for this game?")
        bet = int(input())
        while bet <= 0 or bet > bankroll:
            print("We don't take kindly to jokers round here, make a REAL bet.")
            bet = int(input())
        first_role = roll_dice()
        print(f'You rolled a {first_role}.')
        if first_role == 7 or first_role == 11:
            print('You won!')
            bankroll += bet
            play = play_again()
            continue
        elif first_role in [2, 3, 12,]:
            print('You loose.')
            bankroll -= bet
            play = play_again()
            continue
        else:
            points = first_role
            print('Now things get complicated.')
            # Explain rules here.
            next_role = roll_dice()
            if next_role == first_role:
                print('You win!')
                bankroll += bet
                play = play_again()
                continue
            while next_role != first_role:
                next_role = roll_dice()
                print(next_role)
                if next_role == 7:
                    print('You loose.')
                    bankroll -= bet
                    play = play_again()
                    break
            if next_role == 7:
                continue
            print('You won!')
            bankroll += bet
            play = play_again()
            continue


play_game()
