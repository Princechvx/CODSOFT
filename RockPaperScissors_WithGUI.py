import tkinter as tk
from tkinter import messagebox
import random
import json
import os


class RockPaperScissors:
    def __init__(self, root):
        """
        Initializes the Rock-Paper-Scissors game application with data persistence.
        """
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.geometry("400x500")
        self.file_path = "rps_game_data.json"

        # Load scores from file
        self.user_score = 0
        self.computer_score = 0
        self.load_data()

        # UI Elements
        self.title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=10)

        self.instructions_label = tk.Label(root, text="Choose your move:", font=("Arial", 14))
        self.instructions_label.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.rock_button = tk.Button(self.button_frame, text="Rock", font=("Arial", 14), command=lambda: self.play_game("Rock"))
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = tk.Button(self.button_frame, text="Paper", font=("Arial", 14), command=lambda: self.play_game("Paper"))
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors", font=("Arial", 14), command=lambda: self.play_game("Scissors"))
        self.scissors_button.grid(row=0, column=2, padx=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(root, text=f"Your Score: {self.user_score} | Computer Score: {self.computer_score}", font=("Arial", 14))
        self.score_label.pack(pady=10)

        self.play_again_button = tk.Button(root, text="Reset Game", font=("Arial", 14), command=self.reset_game)
        self.play_again_button.pack(pady=10)

    def play_game(self, user_choice):
        """
        Handles the main game logic: user and computer choices, result determination, and score tracking.
        """
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        # Determine the winner
        if user_choice == computer_choice:
            result = "It's a Tie!"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            result = "You Win!"
            self.user_score += 1
        else:
            result = "You Lose!"
            self.computer_score += 1

        # Save scores to file
        self.save_data()

        # Update the result label
        self.result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")

        # Update the score label
        self.score_label.config(text=f"Your Score: {self.user_score} | Computer Score: {self.computer_score}")

    def reset_game(self):
        """
        Resets the game for another round and optionally deletes saved data.
        """
        confirm = messagebox.askyesno("Reset Game", "Do you want to reset the scores and delete saved data?")
        if confirm:
            self.user_score = 0
            self.computer_score = 0
            if os.path.exists(self.file_path):
                os.remove(self.file_path)
            self.result_label.config(text="")
            self.score_label.config(text="Your Score: 0 | Computer Score: 0")
            messagebox.showinfo("Game Reset", "Scores and saved data have been reset.")
        else:
            self.result_label.config(text="Scores remain unchanged.")

    def save_data(self):
        """
        Saves the current scores to a JSON file.
        """
        data = {"user_score": self.user_score, "computer_score": self.computer_score}
        with open(self.file_path, "w") as file:
            json.dump(data, file)

    def load_data(self):
        """
        Loads the scores from a JSON file if it exists.
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                data = json.load(file)
                self.user_score = data.get("user_score", 0)
                self.computer_score = data.get("computer_score", 0)


if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()
