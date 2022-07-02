import time
import random
from difflib import SequenceMatcher


with open('paragraphs.txt') as data:
    paragraphs = data.readlines()


def accuracy_check(return_type, to_type):
    ratio = SequenceMatcher(None, return_type, to_type).ratio()
    accuracy = int(ratio * 100)
    return accuracy


def calculate_wpm(now, then, char_count):
    word_count = char_count / 5
    minutes = (now - then) / 60
    wpm = int(word_count / minutes)
    return wpm


def game_play():
    n = random.randint(0, len(paragraphs) - 1)
    to_type = paragraphs[n]
    then = time.time()
    return_type = input(f"Type the following and press return when finished: \n{to_type}\n")
    now = time.time()
    return_list = [char for char in return_type]
    char_count = len(return_list)
    accuracy = accuracy_check(return_type, to_type)
    wpm = calculate_wpm(now, then, char_count)



    again = input('\nWould you like to play again? Y or N: ')
    if again.lower() == 'y':
        game_play()


