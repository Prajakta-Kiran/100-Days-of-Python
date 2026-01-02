import art
import random
import hlgameData

#TODO - if guess is wrong , terminate , show final score after logo - Higher or Lower
#TODO - what happens when hldata is empty, add null check everywhere, nedata also


def createNewData(data, gameData):
    """ Wrote this code under the assumption that option a and be will have always random value.
        value should be always different not same"""
    data[0] = random.choice(data)
    data[1] = random.choice(gameData.data)
    gameData.data.remove(data[1])

def play_game():
    print(art.logo)
    keep_guessing = True
    score = 0

    new_data = []

    option_a = random.choice(hlgameData.data)
    hlgameData.data.remove(option_a)
    option_b = random.choice(hlgameData.data)
    hlgameData.data.remove(option_b)

    new_data.append(option_a)
    new_data.append(option_b)

    while keep_guessing and len(hlgameData.data)!=0:
        print(f"Compare A: {new_data[0]['name']}, {new_data[0]['description']} from {new_data[0]['country']}")
        print(art.vs)
        print(f"Against B: {new_data[1]['name']}, {new_data[1]['description']} from {new_data[1]['country']}")

        selected_type = input("Who has more followers? Type 'A' or 'B': ")

        if selected_type.lower() == 'a' :
            if new_data[0]['follower_count'] > new_data[1]['follower_count']:
                score +=1
                createNewData(new_data, hlgameData)
                print(art.logo)
                print(f"You are right! Current score: {score}")
            else:
                keep_guessing = False
                print(f"Wrong guess! Final score: {score}")

        else:
            if new_data[1]['follower_count'] > new_data[0]['follower_count']:
                score +=1
                createNewData(new_data, hlgameData)
                print(art.logo)
                print(f"You are right! Current score: {score}")
            else:
                keep_guessing = False
                print(f"Wrong guess! Final score: {score}")
        
play_game()
