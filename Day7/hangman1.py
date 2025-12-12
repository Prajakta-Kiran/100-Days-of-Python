import random
from hangman_words import word_list

selected_word = random.choice(word_list)
selected_word_list = list(selected_word.lower())
print(selected_word_list)

#blank list with "_" values
result_list = []
for i in range(len(selected_word_list)):
    result_list.append("_")
result_val = "".join(result_list)
print(result_val)

number_of_wrong_guesses = 6

def replaceBlankSpaceWithGuessedLetter(guessed_letter):
    for i in range(len(selected_word_list)):
        if guessed_letter == selected_word_list[i]:
           #find the index of the guessed_letter
           result_list[i] = guessed_letter           

while  selected_word_list != result_list:
    guessed_letter = input("Guess the letter: ")
    if guessed_letter.lower() not in selected_word_list:
        number_of_wrong_guesses -= 1 
        print(f"You have {number_of_wrong_guesses} wrong number of guesses")
    else:         
        replaceBlankSpaceWithGuessedLetter(guessed_letter.lower())
        print("".join(result_list))

    if number_of_wrong_guesses == 0:
        print("Sorry, You can have only 6 wrong number of guesses.")
        break

if(number_of_wrong_guesses!=0):
    print(f"Congratulations!! You guessed the correct word {"".join(result_list)}") 
print("Game over")



   











