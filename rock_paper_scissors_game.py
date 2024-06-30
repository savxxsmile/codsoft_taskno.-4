import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        
        self.user_choice = ""
        self.computer_choice = ""
        self.user_score = 0
        self.computer_score = 0
        
        # Label for instructions
        self.lbl_instructions = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
        self.lbl_instructions.pack(pady=10)
        
        # Buttons for user choices
        self.btn_rock = tk.Button(root, text="Rock", width=10, command=lambda: self.make_choice("rock"))
        self.btn_rock.pack(pady=5)
        
        self.btn_paper = tk.Button(root, text="Paper", width=10, command=lambda: self.make_choice("paper"))
        self.btn_paper.pack(pady=5)
        
        self.btn_scissors = tk.Button(root, text="Scissors", width=10, command=lambda: self.make_choice("scissors"))
        self.btn_scissors.pack(pady=5)
        
        # Label for displaying user and computer choices
        self.lbl_choices = tk.Label(root, text="")
        self.lbl_choices.pack(pady=10)
        
        # Label for displaying result
        self.lbl_result = tk.Label(root, text="")
        self.lbl_result.pack(pady=10)
        
        # Label for displaying scores
        self.lbl_scores = tk.Label(root, text="User: 0 | Computer: 0")
        self.lbl_scores.pack(pady=10)
        
        # Button to play again
        self.btn_play_again = tk.Button(root, text="Play Again", command=self.reset_game, state=tk.DISABLED)
        self.btn_play_again.pack(pady=5)
        
    def make_choice(self, choice):
        self.user_choice = choice
        self.computer_choice = random.choice(["rock", "paper", "scissors"])
        
        # Display user and computer choices
        self.lbl_choices.config(text=f"You chose: {self.user_choice.capitalize()}\nComputer chose: {self.computer_choice.capitalize()}")
        
        # Determine the result
        result = self.determine_winner(self.user_choice, self.computer_choice)
        
        # Display result
        self.lbl_result.config(text=result)
        
        # Update scores
        if result == "You win!":
            self.user_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1
        
        # Update score label
        self.lbl_scores.config(text=f"User: {self.user_score} | Computer: {self.computer_score}")
        
        # Enable play again button
        self.btn_play_again.config(state=tk.NORMAL)
        
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            return "You win!"
        else:
            return "Computer wins!"
    
    def reset_game(self):
        # Reset choices and labels
        self.user_choice = ""
        self.computer_choice = ""
        self.lbl_choices.config(text="")
        self.lbl_result.config(text="")
        
        # Disable play again button until a new choice is made
        self.btn_play_again.config(state=tk.DISABLED)
        
        # Ask if user wants to play again
        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if not play_again:
            self.root.destroy()  # Close the window if user chooses not to play again

# Main function to start the game
def main():
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
