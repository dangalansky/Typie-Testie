import time
import pandas
import random

data = pandas

n = random.randint(0, len(type_list)-1)
type = type_list[n]
char_count = len(type)




before_time = time.time()
input(f"Type the following and press return: \n{type}\n")
after_time = time.time()
time = int(now-then)/60
print(f'Shit! took ya {time}sec to type.')
