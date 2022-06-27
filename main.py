import time
import random

# open paragraphs.txt file
with open('paragraphs.txt') as data:
    paragraphs = data.readlines()

# choose random sentence
def choose_text():
n = random.randint(0, len(paragraphs)-1)
to_type = paragraphs[n]

# calculate word count and character count
word_count = len(list(to_type.split(" ")))
word_list = list(to_type.split(" "))
char_list = [char for char in to_type]
char_count = len(char_list)


print(to_type)
return_type = input(f"Type the following and press return: \n{to_type}\n")

return_list = [char for char in return_type]
return_count = len(return_list)


# accuracy check
def accuracy_check(char_list, return_list)
    inaccuracy = 0

    for character in char_list:
        if character not in return_list:
            inaccuracy += 1

    for character in return_list:
        if character not in char_list:
            inaccuracy += 1

    if return_type == to_type:
        accuracy = 100
    else:
        accuracy = int((return_count / char_count) * 100)

    return accuracy





input(f"Type the following and press return: \n{type}\n")
after_time = time.time()
time = int(now-then)/60
print(f'Shit! took ya {time}sec to type.')
