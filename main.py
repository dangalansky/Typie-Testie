from difflib import SequenceMatcher

# open file to sentences from
with open('paragraphs.txt') as data:
    paragraphs = data.readlines()


# function that compares user's submission to original, returns 'accuracy' as percentage
def accuracy_check(return_type, to_type):
    ratio = SequenceMatcher(None, return_type, to_type).ratio()
    accuracy = int(ratio * 100)
    return accuracy


# function that calculates words per minute based on number of characters in submission
def calculate_wpm(now, then, char_count):
    word_count = char_count / 5
    minutes = (now - then) / 60
    wpm = int(word_count / minutes)
    return wpm
