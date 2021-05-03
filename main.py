"""
Need to clean guess letter input
Uses classes -> No need for Global
Add guess whole word function


TESTING CHANGE

EDIT IN GITHUB
"""
import enchant

def word_checker():  # makes sure the guess word is a real word
    global user_input
    d = enchant.Dict("en_US")
    valid_input = False
    while valid_input == False:
        user_input = input("Which word should they guess?")
        user_input = user_input.strip()
        if len(user_input) > 1 and d.check(user_input):
            valid_input = True
        else:
            pass


def set_up(user_input):  # creates everything needed for guessing part
    global guess_list
    global my_list
    my_list = []
    guess_list = []
    length = len(user_input)  # Make guess list "_" correct length
    for i in range(length):  # this is what the guessers will see
        guess_list.append("_")
    for letters in user_input:
        my_list.append(letters)  # makes list with each letter of guess word a value in string


def guessing(guess_list, my_list):
    global ans
    ans = False
    i = 0
    goes = 0
    attempts = 3
    final_ans = ''.join(my_list)
    print("You have " + str(attempts) + " attempts!")

    while not ans:

        print(guess_list)
        if goes == 3:
            print("You lose, the answer was "+final_ans)
            exit()
        guess = input('guess')
        if guess == final_ans:
            print("Guessed correctly! You win")
            ans = True
            exit()
        if guess in my_list:  # checking if guessed letter in my_list
            print('Correct Guess')
            for letter in my_list:
                if letter == guess:
                    guess_list[i] = letter  # fills the blank section with correct letter
                    i += 1  # 'i' is position in list, we add 1 to represent the change in positon
                else:
                    i += 1
            i = 0
        elif guess not in my_list:
            print("Incorrect Guess")
            goes += 1
            print("You have " + str(attempts - goes) + " attempts left!")

        if guess_list == my_list:
            ans = True
    if ans:
        print("You win")
        win_list = ''.join(guess_list)
        print("The answer was "+str(win_list)+"!")




word_checker()
set_up(user_input)
guessing(guess_list, my_list)
