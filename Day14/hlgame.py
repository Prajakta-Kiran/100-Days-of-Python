from art import logo,vs
from hlgameData import data
import random


keep_guessing = True
option_b = random.choice(data)
score = 0

def format_data(option_data):
    return option_data["name"] + " " + option_data["description"]+ "from " + option_data["country"]

def compare_data(a_followers,b_followers, choice):
    if a_followers > b_followers:
        return choice=='a'
    else:
        return choice=='b'

while keep_guessing:
    option_a = option_b
    if option_a == option_b:
        option_b = random.choice(data)

    print(logo)
    print(f"Compare A:{format_data(option_a)}")
    print(vs)
    print(f"Compare B:{format_data(option_b)}")
    selected_type = input("Who has more followers? Type 'A' or 'B': ")

    a_follower_account = option_a["follower_count"]
    b_follower_account = option_b["follower_count"]
    is_correct = compare_data(a_follower_account, b_follower_account, selected_type)
    if is_correct:
        score += 1
        print(f"You are right! Current score: {score}")
    else:
        keep_guessing = False
        print(f"You are wrong! Final score: {score}")




         






