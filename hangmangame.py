import tkinter as tk
import random

# Word list
fruits = [
    "apple", "banana", "grape", "orange", "mango", "pineapple", "papaya",
    "watermelon", "strawberry", "blueberry", "pear", "peach", "cherry", "kiwi"
]

# Hangman drawing steps
hangman_art = {
    0: ["", "", "", "", "", ""],
    1: ["  O", "", "", "", "", ""],
    2: ["  O", "  |", "", "", "", ""],
    3: ["  O", " /|", "", "", "", ""],
    4: ["  O", " /|\\", "", "", "", ""],
    5: ["  O", " /|\\", " /", "", "", ""],
    6: ["  O", " /|\\", " / \\", "", "", ""]
}

class HangmanGame:
    def __init__(self, master):
        self.master = master
        master.title("Hangman - Fruit Edition")

        self.word = ""
        self.hint = []
        self.guessed_letters = set()
        self.wrong_guesses = 0

        self.title_label = tk.Label(master, text="🍎 Hangman Game 🍌", font=("Helvetica", 20))
        self.title_label.pack(pady=10)

        self.hangman_display = tk.Label(master, text="", font=("Courier", 16), justify="left")
        self.hangman_display.pack()

        self.hint_label = tk.Label(master, text="", font=("Courier", 24))
        self.hint_label.pack(pady=10)

        self.entry = tk.Entry(master, font=("Courier", 16))
        self.entry.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.make_guess)
        self.guess_button.pack(pady=5)

        self.message_label = tk.Label(master, text="", font=("Helvetica", 14))
        self.message_label.pack(pady=5)

        self.restart_button = tk.Button(master, text="Start New Game", command=self.start_game)
        self.restart_button.pack(pady=10)

        self.start_game()

    def start_game(self):
        self.word = random.choice(fruits)
        self.hint = ["_"] * len(self.word)
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.entry.config(state=tk.NORMAL)
        self.guess_button.config(state=tk.NORMAL)
        self.update_display()
        self.message_label.config(text="")
        self.entry.delete(0, tk.END)

    def update_display(self):
        self.hangman_display.config(text="\n".join(hangman_art[self.wrong_guesses]))
        self.hint_label.config(text=" ".join(self.hint))

    def make_guess(self):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            self.message_label.config(text="Invalid input! Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            self.message_label.config(text=f"You already guessed '{guess}'")
            return

        self.guessed_letters.add(guess)

        if guess in self.word:
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.hint[i] = guess
            self.message_label.config(text="Correct!")
        else:
            self.wrong_guesses += 1
            self.message_label.config(text="Wrong guess!")

        self.update_display()
        self.check_game_over()

    def check_game_over(self):
        if "_" not in self.hint:
            self.message_label.config(text="🎉 You Win! 🎉")
            self.entry.config(state=tk.DISABLED)
            self.guess_button.config(state=tk.DISABLED)
        elif self.wrong_guesses >= len(hangman_art) - 1:
            self.hint_label.config(text=self.word)
            self.message_label.config(text="💀 You Lose! 💀")
            self.entry.config(state=tk.DISABLED)
            self.guess_button.config(state=tk.DISABLED)

# Start GUI app
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
