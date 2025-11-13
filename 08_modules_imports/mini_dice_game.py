# imoprt random 
# create two lists for scores for two players and a scoreboard dictionary
# scoreboard = {"Player1":0,"Player2":0,"Ties":0}
# create function to handle the random number and other to check is positive integer
# def roll_a_die():
#   return random number from 1 to 6
# def is_number(n):
#   try:
#       return int(n)
#   execept value error:
#       return none
# def play_round():
#   player_1 = rool_a_die()
#   player_2 = rool_a_die()
#   print Player 1 rolls: {player_1}
#   print Player 2 rolls: {player_2}
#   score 1 += player_1
#   score 2 += player_2
#   if player_1 - player_2 > 0:
#       print Winner: Player 1
#       scoreboard["Player1"] += 1
#   elif player_1 - player_2 < 0:
#       print Winner: Player 2
#       scoreboard["Player2"] += 1
#   else:
#       print Result : Tie
#       scoreboard["Ties"] += 1
#   
# while true:
#   ask user for number
#   if is_number(userinput) is none:
#       print a message
#       continue
#   for i in range(1,number+1):
#       round()
# print the results
# print the dictionary
# print the total points
# if total1 > total2:
#     print("Player 1 wins!")
# elif total2 > total1:
#     print("Player 2 wins!")
# else:
#     print("It's a tie!")


import random

score_1 = 0
score_2 = 0
scoreboard = {"Player1":0,"Player2":0,"Ties":0}

def roll_a_die():
    return random.randint(1,6)

def is_number(n):
    try:
        return int(n)
    except ValueError:
        return None
    
def play_round():
    player_1 = roll_a_die()
    player_2 = roll_a_die()

    print(f"Player 1 rolls : {player_1}")
    print(f"Player 2 rolls : {player_2}")

    if player_1 > player_2:
        scoreboard["Player1"] += 1
        print("Winner: Player 1")
    
    elif player_2 > player_1:
        scoreboard["Player2"] += 1
        print("Winner: Player 2")

    else:
        scoreboard["Ties"] += 1
        print("Result: Tie")

    return player_1, player_2

def winner():
    if scoreboard["Player1"] > scoreboard["Player2"]:
        print("Overall Winner: Player 1 🎉")
    elif scoreboard["Player2"] > scoreboard["Player1"]:
        print("Overall Winner: Player 2 🎉")
    else:
        if score_1 > score_2:
            print("Overall Winner: Player 1 🎉")
        elif score_2 > score_1:
            print("Overall Winner: Player 2 🎉")
        else:
            print("It's a tie.")

while True:
    rounds = input("How many rounds?: ").strip()
    if is_number(rounds) is None:
        print("Invalid input. Enter a valid integer.\n")
        continue
    rounds = int(rounds)
    if rounds <= 0:
        print("Rounds must be bigger than 0.\n")
        continue
    print()
    print()
    for i in range(1, rounds+1):
        print(f"\n— Round {i} —")
        p1, p2 = play_round()
        score_1 += p1
        score_2 += p2
    
    print("\n===== Final Scoreboard =====")

    print(f"Rounds won — Player 1: {scoreboard['Player1']} | Player 2: {scoreboard['Player2']} | Ties: {scoreboard['Ties']}")
    print(f"Total points — Player 1: {score_1} | Player 2: {score_2}")
    winner()
    print("\nThanks for playing! 👋")
    break