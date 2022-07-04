from main import *
import random
import time
from tkinter import *
from PIL import ImageTk, Image


# ------------ Functions ------------- #

def start_type(event):
    canvas.itemconfig(background, image=start_screen)
    type_entry = Entry(width=80)
    type_entry.place(x=100, y=480)
    type_entry.focus()
    n = random.randint(0, len(paragraphs) - 1)
    to_type = paragraphs[n]
    then = time.time()
    type_this = canvas.create_text(470, 430, text=to_type, font=('Helvetica', 16))
    window.bind('<Return>', lambda event: show_results(event, type_entry, type_this, then, to_type))


def show_results(event, type_entry, type_this, then, to_type):
    now = time.time()
    canvas.itemconfig(type_this, text="")
    canvas.itemconfig(background, image=end_screen)
    return_type = type_entry.get()
    type_entry.place_forget()
    return_list = [char for char in return_type]
    char_count = len(return_list)
    accuracy = accuracy_check(return_type, to_type)
    wpm = calculate_wpm(now, then, char_count)
    acc_text = canvas.create_text(255, 485, text=f'{accuracy}%', font=('Helvetica', 40,), fill='red')
    wpm_text = canvas.create_text(695, 485, text=wpm, font=('Helvetica', 40, 'italic'), fill='red')
    window.bind('<Return>', lambda event: restart_type(event, acc_text, wpm_text))
    window.bind('q', quit)


def restart_type(event, acc_text, wpm_text):
    canvas.itemconfig(acc_text, text="")
    canvas.itemconfig(wpm_text, text="")
    canvas.itemconfig(background, image=start_screen)
    type_entry = Entry(width=80)
    type_entry.place(x=100, y=480)
    type_entry.focus()
    n = random.randint(0, len(paragraphs) - 1)
    to_type = paragraphs[n]
    then = time.time()
    type_this = canvas.create_text(470, 430, text=to_type, font=('Helvetica', 16))
    window.bind('<Return>', lambda event: show_results(event, type_entry, type_this, then, to_type))


def quit(event):
    window.destroy()


# ------------ GUI ------------- #
window = Tk()
window.title('Typie Testie')
window.geometry('937x625')

# ------------ Format Images ------------- #
game_open = Image.open('typie_testie.png')
game_open_sm = game_open.resize((937, 625), Image.ANTIALIAS)
open_screen = ImageTk.PhotoImage(game_open_sm)

game_start = Image.open('go.png')
game_start_sm = game_start.resize((937, 625), Image.ANTIALIAS)
start_screen = ImageTk.PhotoImage(game_start_sm)

results = Image.open('results.png')
results_sm = results.resize((937, 625), Image.ANTIALIAS)
end_screen = ImageTk.PhotoImage(results_sm)

# ------------Canvas------------- #
canvas = Canvas(height=625, width=937, bg='black', highlightthickness=0)
background = canvas.create_image(468, 310, image=open_screen)
canvas.place(x=0, y=0)
window.bind('<Return>', start_type)
window.mainloop()
