import tkinter as tk
import random

# -----------------------------
# GAME VARIABLES
# -----------------------------

current_row = 0
current_col = 0

words = [
    "APPLE",
    "HOUSE",
    "PLANT",
    "TRAIN",
    "MOUSE",
    "CHAIR",
    "WATER",
    "PHONE",
    "WORLD",
    "LIGHT",
    "BREAD",
    "MUSIC",
    "PIZZA",
    "BEACH",
    "CLOUD"
]

secret_word = random.choice(words)



# -----------------------------
# MAIN WINDOW
# -----------------------------

root = tk.Tk()
root.title("Python Wordle")
root.geometry("1000x1000")
root.resizable(False, False)


# -----------------------------
# TITLE
# -----------------------------

title = tk.Label(
    root,
    text="WORDLE",
    font=("Arial", 32, "bold")
)

title.pack(pady=20)


# -----------------------------
# GAME BOARD
# -----------------------------

board = tk.Frame(root)
board.pack()

tiles = []

for row in range(6):

    row_tiles = []

    for col in range(5):

        tile = tk.Label(
            board,
            text="",
            width=4,
            height=2,
            font=("Arial", 22, "bold"),
            relief="solid",
            borderwidth=1
        )

        tile.grid(
            row=row,
            column=col,
            padx=4,
            pady=4
        )

        row_tiles.append(tile)

    tiles.append(row_tiles)


# -----------------------------
# CHECK WORD
# -----------------------------

def check_word(guess):

    for i in range(5):

        letter = guess[i]

        if letter == secret_word[i]:

            tiles[current_row][i].config(
                bg="green",
                fg="white"
            )

        elif letter in secret_word:

            tiles[current_row][i].config(
                bg="gold",
                fg="white"
            )

        else:

            tiles[current_row][i].config(
                bg="gray",
                fg="white"
            )


# -----------------------------
# KEY PRESSED
# -----------------------------

def key_pressed(event):

    global current_col

    key = event.keysym.upper()

    if len(key) == 1 and key.isalpha():

        if current_col < 5:

            tiles[current_row][current_col].config(
                text=key
            )

            current_col += 1


# -----------------------------
# ENTER PRESSED
# -----------------------------

def enter_pressed(event):

    global current_row
    global current_col

    if current_col == 5:

        word = ""

        for col in range(5):
            word += tiles[current_row][col]["text"]

        print("Your guess:", word)

        check_word(word)

        if word == secret_word:

            print("YOU WIN!")

        else:

            print("Wrong word!")

        current_row += 1
        current_col = 0


# -----------------------------
# ON-SCREEN KEYBOARD
# -----------------------------

keyboard = tk.Frame(root)
keyboard.pack(pady=30)


# Keyboard rows
keyboard_rows = [
    "QWERTYUIOP",
    "ASDFGHJKL",
    "ZXCVBNM"
]


def keyboard_click(letter):

    global current_col

    if current_col < 5:

        tiles[current_row][current_col].config(
            text=letter
        )

        current_col += 1


for row_letters in keyboard_rows:

    row_frame = tk.Frame(keyboard)
    row_frame.pack()

    for letter in row_letters:

        button = tk.Button(
            row_frame,
            text=letter,
            width=4,
            height=2,
            font=("Arial", 12, "bold"),
            command=lambda l=letter: keyboard_click(l)
        )

        button.pack(
            side="left",
            padx=2,
            pady=2
        )


# -----------------------------
# KEYBOARD EVENTS
# -----------------------------

root.bind("<Key>", key_pressed)
root.bind("<Return>", enter_pressed)


# -----------------------------
# START GAME
# -----------------------------

root.mainloop()