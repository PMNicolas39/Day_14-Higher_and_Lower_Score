from art import logo, vs
from game_data import data
import random
import os


# iterate the data[i] from list
def get_random_data():
    return random.choice(data)


is_game_over = False
score = 0
while not is_game_over:
    print(logo)
    a = get_random_data()
    b = get_random_data()

    while a == b:
        b = get_random_data()

    A_follower = a['follower_count']
    print(f"Compare A: {a['name']},  {a['description']}, from {a['country']}")

    print(vs)

    B_follower = b['follower_count']
    print(f"Opponent B: {b['name']},  {b['description']}, from {b['country']}")

    guess = input("who has more follower? Type 'A' or 'B': ")
    os.system('cls')
    if A_follower > B_follower:
        score += 1
        print(f"you're right! current score = {score}")
    else:
        score = score
        print(f"you're wrong! current score = {score}")
        is_game_over = True
