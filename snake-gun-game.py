import tkinter as tk
import random

# Game choices
choices = ["Snake", "Water", "Gun"]

# Function to decide winner
def play(user_choice):
    computer_choice = random.choice(choices)

    result_text.set(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        winner_text.set("Result: It's a Tie 😄")

    elif (
        (user_choice == "Snake" and computer_choice == "Water") or
        (user_choice == "Water" and computer_choice == "Gun") or
        (user_choice == "Gun" and computer_choice == "Snake")
    ):
        winner_text.set("Result: You Win 🎉")

    else:
        winner_text.set("Result: Computer Wins 🤖")


# Create main window
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("400x350")
root.config(bg="#1e1e1e")

# Title Label
title = tk.Label(root, text="🐍 Snake 💧 Water 🔫 Gun",
                 font=("Arial", 18, "bold"),
                 bg="#1e1e1e", fg="white")
title.pack(pady=20)

# Result Variables
result_text = tk.StringVar()
winner_text = tk.StringVar()

# Result Labels
result_label = tk.Label(root, textvariable=result_text,
                        font=("Arial", 12),
                        bg="#1e1e1e", fg="lightgreen")
result_label.pack(pady=10)

winner_label = tk.Label(root, textvariable=winner_text,
                        font=("Arial", 14, "bold"),
                        bg="#1e1e1e", fg="yellow")
winner_label.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=20)

snake_btn = tk.Button(btn_frame, text="🐍 Snake",
                      width=12, command=lambda: play("Snake"))
snake_btn.grid(row=0, column=0, padx=10)

water_btn = tk.Button(btn_frame, text="💧 Water",
                      width=12, command=lambda: play("Water"))
water_btn.grid(row=0, column=1, padx=10)

gun_btn = tk.Button(btn_frame, text="🔫 Gun",
                    width=12, command=lambda: play("Gun"))
gun_btn.grid(row=0, column=2, padx=10)

# Run application
root.mainloop()