import art
import random
import hlgameData

#TODO - if guess is wrong , terminate , show final score after logo - Higher or Lower
#TODO - what happens when hldata is empty, add null check everywhere, nedata also


def createNewData(data, gameData):
    """ Wrote this code under the assumption that option a and be will have always randome value. 
        value shoud be always different not same"""
    data[0] = random.choice(data)
    data[1] = random.choice(gameData.data)
    gameData.data.remove(data[1])

def play_game():
    print(art.logo)
    keepGuessing = True
    score = 0

    newData = []
    option_a = {}
    option_b = {}
 
    option_a = random.choice(hlgameData.data)
    hlgameData.data.remove(option_a)
    option_b = random.choice(hlgameData.data)
    hlgameData.data.remove(option_b)

    newData.append(option_a)
    newData.append(option_b)

    while keepGuessing and len(hlgameData.data)!=0:
        print(f"Compare A: {newData[0]['name']}, {newData[0]['description']} from {newData[0]['country']}")
        print(art.vs)
        print(f"Against B: {newData[1]['name']}, {newData[1]['description']} from {newData[1]['country']}")

        selected_type = input("Who has more followers? Type 'A' or 'B': ")

        if selected_type.lower() == 'a' :
            if newData[0]['follower_count'] > newData[1]['follower_count']:
                score +=1
                createNewData(newData, hlgameData)
                print(art.logo)
                print(f"You are right! Current score: {score}")
            else:
                keepGuessing = False
                print(f"Wrong guess! Final score: {score}")

        else:
            if newData[1]['follower_count'] > newData[0]['follower_count']:
                score +=1
                createNewData(newData, hlgameData)
                print(art.logo)
                print(f"You are right! Current score: {score}")
            else:
                keepGuessing = False
                print(f"Wrong guess! Final score: {score}")
        
play_game()
