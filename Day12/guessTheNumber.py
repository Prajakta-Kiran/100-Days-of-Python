import random
print("Welcome to number guessing game!")
print("I am thinking number between 1 to 100.")
difficulty = input("Choose difficulty. Type 'Easy' or 'hard: ")
ACTUAL_NUMBER = random.choice(range(1,101))
correctGuess = True

def getAttempts(difficulty):
    if difficulty == 'hard':
        return 5
    else:
        return 10
    
def compareNum(playerGuessedNum):
    if playerGuessedNum == ACTUAL_NUMBER:
        print(f"Bravo! You guessed the correct number {ACTUAL_NUMBER}")
        return True
    elif playerGuessedNum < ACTUAL_NUMBER:
        print("Too low.\nGuess again.")
        return False
    else:
        print("Too high.\nGuess again.")
        return False
    
def guessTheNumber(difficulty):
    attempts = getAttempts(difficulty)
    while attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guessed_num = int(input("Make a guess: "))
        attempts-=1
        correctGuess = compareNum(guessed_num)
        if correctGuess:
            attempts = 0  
    if not correctGuess:
        print("You have run out of the guesses.Refresh page to start again.")

guessTheNumber(difficulty) 



