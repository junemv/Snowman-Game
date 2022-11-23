import random
from wonderwords import RandomWord
#https://pypi.org/project/wonderwords/

# used by word randomizer
SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_MIN_WORD_LENGTH = 5

#max number of wrong guesses
SNOWMAN_WRONG_GUESSES = 7

SNOWMAN_GRAPHIC = [
'*   *   *  ', 
' *   _ *   ', 
'   _[_]_ * ', 
'  * (")    ', 
'  \( : )/ *', 
'* (_ : _)  ', 
'-----------'
]

def print_snowman(wrong_guesses_count):
    for i in range(SNOWMAN_WRONG_GUESSES - wrong_guesses_count, SNOWMAN_WRONG_GUESSES):
        print(SNOWMAN_GRAPHIC[i])

def snowman():
    r = RandomWord()
    snowman_word = r.word(
        word_min_length=SNOWMAN_MIN_WORD_LENGTH, 
        word_max_length=SNOWMAN_MAX_WORD_LENGTH)
    # print(f"debug snowman_word: {snowman_word}") #use this if you're a cheater

    # stores each letter of the randomized word as key - False as default value, True if guessed by user
    snowman_word_dict = build_word_dict(snowman_word)

    # stores each wrong lettter
    wrong_guesses_list = []

    word_complete_flag = False

    while word_complete_flag == False and len(wrong_guesses_list) != SNOWMAN_WRONG_GUESSES:
        user_letter = get_letter_from_user(wrong_guesses_list, snowman_word_dict)

        if user_letter in snowman_word_dict:
            print(" ")
            print("Letter found!")
            snowman_word_dict[user_letter] = True
        else:
            print(" ")
            print(f"The letter {user_letter} was not found in word")
            wrong_guesses_list.append(user_letter)
        
        if get_word_progress(snowman_word_dict):
            word_complete_flag = True
        
        print(" ")
        print_snowman(len(wrong_guesses_list))
        print(" ")
        print(f"Word progress: {print_word_progress_string(snowman_word, snowman_word_dict)}")
        print(f"Wrong guesses: {wrong_guesses_list}")

        if len(wrong_guesses_list) == SNOWMAN_WRONG_GUESSES:
            print(" ")
            print("GAME OVER")
            print("But on the bright side, you built a cute snowperson!")
            print(" ")
            print(f"The word was: {snowman_word}")
            print(f"~You made {correct_letter_counter(snowman_word_dict)} correct and {len(wrong_guesses_list)} incorrect guesses~")


    if word_complete_flag:
        print(" ")
        print("CONGRATULATIONS!!")
        print(" ")
        print("You've won! Our poor snowperson will remain unfinished...")
        print(f"The word was: {snowman_word}")

    print(" ")
    print("...")
    print(" ")
    replay_game()

def get_letter_from_user(wrong_guesses_list, snowman_word_dict):
    # Helper function - requests and checks user input
    check_letter = False
    user_input_string = None

    while check_letter == False:
        user_input_string = input("Guess one letter: ")
    
        if not user_input_string.isalpha():
            print("You must input a letter!")
            print(" ")    
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
            print(" ")
        elif user_input_string in snowman_word_dict and snowman_word_dict[user_input_string]:
            print("You have already guessed that letter and it's in the word!")
            print(" ")
        elif user_input_string in wrong_guesses_list:
            print("You have already guessed that letter!")
            print(" ")
        else:
            check_letter = True

    return user_input_string

def build_word_dict(word):
    # Helper function - generates dictionary used in snowman function
    # Dictionary - each letter in randomized word as keys, False as values
    snowman_word_dict = {}

    for letter in word:
        snowman_word_dict[letter] = False
        
    return snowman_word_dict

def print_word_progress_string(snowman_word, snowman_word_dict):
    # generates and returns a string that shows user's progress in guessing the word
    word_progress = ""
    counter = 0

    for letter in snowman_word:
        if counter > 0:
            word_progress += " "
        if not snowman_word_dict[letter]:
            word_progress += "_"
        else:
            word_progress += letter
        
        counter += 1
    
    return word_progress

def get_word_progress(snowman_word_dict):
    # returns True if the word is complete
    # word_complete_flag
    for letter in snowman_word_dict:
        if not snowman_word_dict[letter]:
            return False
        
    return True

def correct_letter_counter(snowman_word_dict):
    correct_letters = 0
    for letter in snowman_word_dict:
        if snowman_word_dict[letter] == True:
            correct_letters += 1
    
    return correct_letters

def replay_game():
    # helper function - returns true or false based on user input
    loop_flag = 0

    while loop_flag < 1:
        replay_check = input("would you like to play again(yes/no)? ")

        if replay_check == 'yes' or replay_check == 'Yes':
            loop_flag += 1
            print(" ")
            play_game_no_intro()
        elif replay_check == 'no' or replay_check == 'No':
            loop_flag += 1
            print(" ")
            print("Thanks for playing!")
        else:
            print("You must input 'yes' or 'no'")
            print(" ")

def play_game():
    print("Let's play a word guessing game!")
    print(" ")
    print("-For each wrong letter the snowperson will get bigger")
    print("-If they reach max size, you lose!")
    print("-Guess the complete word to win!")
    print(" ")
    print("Let's start...")
    snowman()

def play_game_no_intro():
    snowman()
play_game()