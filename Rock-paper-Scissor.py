import tkinter as tk
import random
import winsound  # Built-in (Windows only)

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Rock Paper Scissors 🔥")
root.geometry("520x550")
root.configure(bg="#1f1f2e")
root.resizable(False, False)

# ---------------- VARIABLES ----------------
user_score = 0
computer_score = 0
choices = ["Rock", "Paper", "Scissors"]

# ---------------- SOUND FUNCTIONS ----------------
def play_click_sound():
    winsound.Beep(800, 150)  # frequency, duration

def play_win_sound():
    winsound.Beep(1000, 200)
    winsound.Beep(1200, 200)

def play_lose_sound():
    winsound.Beep(400, 400)

# ---------------- GAME FUNCTION ----------------
def play(user_choice):
    global user_score, computer_score

    play_click_sound()

    computer_choice = random.choice(choices)

    result_text.set(f"You: {user_choice}   |   Computer: {computer_choice}")

    if user_choice == computer_choice:
        result = "🤝 It's a Tie!"
        root.configure(bg="#2e2e3f")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        user_score += 1
        result = "🎉 You Win!"
        play_win_sound()
        root.configure(bg="#1f3f2e")
    else:
        computer_score += 1
        result = "💻 Computer Wins!"
        play_lose_sound()
        root.configure(bg="#3f1f2e")

    result_label.config(text=result)
    score_label.config(text=f"Your Score: {user_score}    Computer Score: {computer_score}")

# ---------------- RESET ----------------
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_text.set("")
    result_label.config(text="")
    score_label.config(text="Your Score: 0    Computer Score: 0")
    root.configure(bg="#1f1f2e")

# ---------------- HOVER EFFECT ----------------
def on_enter(e):
    e.widget['background'] = "#ff4c4c"

def on_leave(e):
    e.widget['background'] = "#ff6b6b"

# ---------------- UI DESIGN ----------------
title = tk.Label(root, text="Rock Paper Scissors",
                 font=("Helvetica", 24, "bold"),
                 bg="#1f1f2e", fg="white")
title.pack(pady=25)

result_text = tk.StringVar()
result_display = tk.Label(root, textvariable=result_text,
                          font=("Helvetica", 14),
                          bg="#1f1f2e", fg="#00ffff")
result_display.pack(pady=10)

result_label = tk.Label(root, text="",
                        font=("Helvetica", 20, "bold"),
                        bg="#1f1f2e", fg="#ffd700")
result_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#1f1f2e")
button_frame.pack(pady=35)

btn_style = {
    "width": 12,
    "font": ("Helvetica", 14, "bold"),
    "bg": "#ff6b6b",
    "fg": "white",
    "bd": 0,
    "activebackground": "#ff4c4c"
}

rock_btn = tk.Button(button_frame, text="🪨 Rock",
                     command=lambda: play("Rock"), **btn_style)
rock_btn.grid(row=0, column=0, padx=15)

paper_btn = tk.Button(button_frame, text="📄 Paper",
                      command=lambda: play("Paper"), **btn_style)
paper_btn.grid(row=0, column=1, padx=15)

scissor_btn = tk.Button(button_frame, text="✂ Scissors",
                        command=lambda: play("Scissors"), **btn_style)
scissor_btn.grid(row=0, column=2, padx=15)

for btn in [rock_btn, paper_btn, scissor_btn]:
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

score_label = tk.Label(root, text="Your Score: 0    Computer Score: 0",
                       font=("Helvetica", 14),
                       bg="#1f1f2e", fg="white")
score_label.pack(pady=20)

reset_btn = tk.Button(root, text="Reset Game",
                      font=("Helvetica", 13, "bold"),
                      bg="#00b894", fg="white",
                      command=reset_game)
reset_btn.pack(pady=15)

root.mainloop()