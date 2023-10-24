import tkinter as tk
import random

"""play rock paper scissors with the computer"""


# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
            (user_choice == "Scissors" and computer_choice == "Paper") or \
            (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "Computer wins!"


# Function to handle user selection
def user_choice(selection):
    computer_selection = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(selection, computer_selection)
    result_label.config(text=f"Computer Chose: {computer_selection}\n{result}")


# Set up the tkinter window
root = tk.Tk()
root.geometry("300x200")
root.title("Rock Paper Scissors")

# Create the buttons
rock_button = tk.Button(root, text="Rock", command=lambda: user_choice("Rock"))
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", command=lambda: user_choice("Paper"))
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: user_choice("Scissors"))
scissors_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the main loop
root.mainloop()
