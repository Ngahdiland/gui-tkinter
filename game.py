
import tkinter as tk
from random import randint

class GuessingGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Guessing Game")
        self.number_to_guess = randint(1, 100)
        self.trials = 3

        self.guess_label = tk.Label(self.root, text="Guess a number between 1 and 100:", font=("Arial", 24, "bold"), bg="#44c1e0", fg="#FFFFFF")
        self.guess_label.pack( padx=20, pady=20)

        self.guess_entry = tk.Entry(self.root, font=("Arial", 16))
        self.guess_entry.pack()

        self.result_label = tk.Label(self.root, text="")

        self.result_label.pack()

        self.guess_button = tk.Button(self.root, text="Guess", font=("Arial", 
        16), bg="#000000", fg="#FFFFFF", padx=10, command=self.check_guess)
        self.guess_button.pack()

        self.reset_button = tk.Button(self.root, text="Reset", font=("Arial", 
        16), bg="#c7ebe0", fg="#ff0505", padx=10, command=self.reset_game)
        self.reset_button.pack()

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            self.result_label['text'] = "Invalid input. Please enter a number."
            return

        self.trials -= 1

        if guess == self.number_to_guess:
            self.result_label['text'] = "You are smart! You guessed the number in {} trials.".format(3 - self.trials)
            self.guess_button['state'] = 'disabled'
        elif guess < self.number_to_guess:
            self.result_label['text'] = "Your guess is too low. Try again. Trials remaining: {}".format(self.trials)
        else:
            self.result_label['text'] = "Your guess is too high. Try again. Trials remaining: {}".format(self.trials)

        if self.trials == 0:
            self.result_label['text'] = "Game over. The number was {}. Better luck next time.".format(self.number_to_guess)
            self.guess_button['state'] = 'disabled'

    def reset_game(self):
        self.number_to_guess = randint(1, 100)
        self.trials = 3
        self.guess_entry.delete(0, tk.END)
        self.result_label['text'] = ""
        self.guess_button['state'] = 'normal'

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = GuessingGame()
    game.run()
