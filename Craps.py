#Alex Bello
#10/23/2019

import random


def rolldice():
    roll = random.randint(2, 12)
    return roll


def create():
    print("How much money is in your starting bankroll?")
    return int(input())


bankroll = create()
print(f"How much ya wanna put up from ${bankroll} for this game?")
bet = int(input())
while bet <= 0:
    print("We don't take kindly to jokers round here, make a REAL bet.")
    bet = int(input())

while bankroll > 0 and bet > 0:
    rolldice()



