import random

startNewGame = True
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def calculate_score(player_cards, computer_cards):
    player_score = 0
    computer_score = 0

    for i in player_cards:
        player_score +=i
    
    for i in computer_cards:
        computer_score +=i

    scores = {"p_score" : player_score, "c_score": computer_score}
    print(f"Your card: {player_cards} , current_score:  {player_score}")
    print(f"Computer's first card: {computer_cards[0]}")  
    return scores

def gameCalculations():
    player_cards = random.choices(cards, k=2)
    computer_cards = random.choices(cards, k=2)
    continue_game = True

    while continue_game:
        scores = calculate_score(player_cards, computer_cards)
        if scores['p_score'] > 21 and 11 in player_cards:
            player_cards.remove(11)
            player_cards.append(1)
        elif scores['p_score'] > 21:
            continue_game = False
            print("You went over. You lose. :-(")
        elif scores['p_score'] == 21:
            continue_game = False
            print("Congrats!! You won :-)")
        else :
            fetch_card = input("Type 'y' to fetch another card,'n' to pass: ")
            if fetch_card == 'y':
                player_cards.append(random.choice(cards))
                if scores['c_score']<=17:
                    computer_cards.append(random.choice(cards))
            else:
                continue_game = False
                if scores['p_score']<scores['c_score']:
                    print("You Lose :-(. Opponent wins")
                elif scores['p_score']==scores['c_score']:
                     print("Its a draw.")
                else:     
                    print("Congrats! You win :-)")
    print(f"Your final hand: {player_cards} , Final score: {scores['p_score']}")
    print(f"Computer's final hand: {computer_cards}, Final score: {scores['c_score']}")

    
while startNewGame:
    response = input("Do you want to play game of blackjack? Type 'y' or 'n': ")
    if response == 'y':
        gameCalculations()
    else:
        startNewGame = False
        print("Thanks for playing BlackJackCapstone Game!")
        




           




    