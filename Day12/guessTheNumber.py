import random
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

#TODO : Easy and hard constants.

def getAttempts(difficulty):
    if difficulty == 'hard':
        return HARD_ATTEMPTS
    else:
        return EASY_ATTEMPTS
    
def compareNum(playerGuessedNum, actual_num):
    if playerGuessedNum == actual_num:
        print(f"Bravo! You guessed the correct number {actual_num}")
        return True
    elif playerGuessedNum < actual_num:
        print("Too low.\nGuess again.")
        return False
    else:
        print("Too high.\nGuess again.")
        return False
    
def guessTheNumber():
    print("Welcome to number guessing game!")
    print("I am thinking number between 1 to 100.")
    difficulty = input("Choose difficulty. Type 'easy' or 'hard: ")
    actual_num = random.randint(1,100)
    correctGuess = True

    attempts = getAttempts(difficulty)
    while attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guessed_num = int(input("Make a guess: "))
        attempts-=1
        correctGuess = compareNum(guessed_num, actual_num)
        if correctGuess:
            attempts = 0  
    if not correctGuess:
        print("You have run out of the guesses.Refresh page to start again.")

guessTheNumber() 



