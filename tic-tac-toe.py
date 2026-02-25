import tkinter as tk
import random
import winsound

# ------------------ MAIN WINDOW ------------------
root = tk.Tk()
root.title("Tic Tac Toe Pro")
root.geometry("420x550")
root.config(bg="#1e1e2f")

board = [""] * 9
buttons = []
current_player = "X"
game_mode = None  # "2P" or "AI"

# ------------------ SOUND FUNCTIONS ------------------

def play_click_sound():
    winsound.Beep(800, 100)

def play_start_sound():
    winsound.Beep(600, 150)
    winsound.Beep(800, 150)

def play_win_sound():
    winsound.Beep(1000, 200)
    winsound.Beep(1200, 200)
    winsound.Beep(1400, 200)

def play_draw_sound():
    winsound.Beep(400, 300)

# ------------------ GAME LOGIC ------------------

def select_mode(mode):
    global game_mode
    game_mode = mode
    menu_frame.pack_forget()
    game_frame.pack()
    reset_game()
    play_start_sound()

def click(index):
    global current_player

    if board[index] == "" and not check_winner():
        board[index] = current_player
        buttons[index].config(text=current_player)
        play_click_sound()

        if check_winner():
            status_label.config(text=f"🎉 Player {current_player} Wins!")
            play_win_sound()
            return
        elif "" not in board:
            status_label.config(text="😐 It's a Draw!")
            play_draw_sound()
            return

        current_player = "O" if current_player == "X" else "X"
        status_label.config(text=f"Player {current_player}'s Turn")

        if game_mode == "AI" and current_player == "O":
            root.after(500, computer_move)

def computer_move():
    global current_player

    move = get_best_move("O")
    if move is None:
        empty_indices = [i for i in range(9) if board[i] == ""]
        move = random.choice(empty_indices)

    board[move] = "O"
    buttons[move].config(text="O")
    play_click_sound()

    if check_winner():
        status_label.config(text="🤖 Computer Wins!")
        play_win_sound()
        return
    elif "" not in board:
        status_label.config(text="😐 It's a Draw!")
        play_draw_sound()
        return

    current_player = "X"
    status_label.config(text="Player X's Turn")

def get_best_move(player):
    opponent = "X" if player == "O" else "O"
    win_positions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    # Try to win
    for a,b,c in win_positions:
        line = [board[a], board[b], board[c]]
        if line.count(player) == 2 and line.count("") == 1:
            if board[a] == "":
                return a
            if board[b] == "":
                return b
            if board[c] == "":
                return c

    # Block opponent
    for a,b,c in win_positions:
        line = [board[a], board[b], board[c]]
        if line.count(opponent) == 2 and line.count("") == 1:
            if board[a] == "":
                return a
            if board[b] == "":
                return b
            if board[c] == "":
                return c

    return None

def suggest_move():
    move = get_best_move(current_player)
    if move is None:
        empty = [i for i in range(9) if board[i] == ""]
        if empty:
            move = random.choice(empty)

    if move is not None:
        buttons[move].config(bg="#00ffcc")
        root.after(800, lambda: buttons[move].config(bg="#2b2b40"))

def check_winner():
    win_positions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in win_positions:
        if board[a] == board[b] == board[c] != "":
            return True
    return False

def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    status_label.config(text="Player X's Turn")
    for btn in buttons:
        btn.config(text="", bg="#2b2b40")

def back_to_menu():
    game_frame.pack_forget()
    menu_frame.pack()

# ------------------ MENU FRAME ------------------

menu_frame = tk.Frame(root, bg="#1e1e2f")

tk.Label(menu_frame, text="Tic Tac Toe Pro",
         font=("Arial", 26, "bold"),
         bg="#1e1e2f", fg="white").pack(pady=30)

tk.Button(menu_frame, text="2 Player Mode",
          font=("Arial", 14),
          bg="#4CAF50", fg="white",
          width=20,
          command=lambda: select_mode("2P")).pack(pady=10)

tk.Button(menu_frame, text="Play With Computer",
          font=("Arial", 14),
          bg="#2196F3", fg="white",
          width=20,
          command=lambda: select_mode("AI")).pack(pady=10)

menu_frame.pack()

# ------------------ GAME FRAME ------------------

game_frame = tk.Frame(root, bg="#1e1e2f")

status_label = tk.Label(game_frame,
                        text="Player X's Turn",
                        font=("Arial", 16, "bold"),
                        bg="#1e1e2f",
                        fg="white")
status_label.pack(pady=15)

board_frame = tk.Frame(game_frame, bg="#1e1e2f")
board_frame.pack()

for i in range(9):
    btn = tk.Button(board_frame,
                    text="",
                    font=("Arial", 24, "bold"),
                    width=5,
                    height=2,
                    bg="#2b2b40",
                    fg="white",
                    activebackground="#444466",
                    command=lambda i=i: click(i))
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

tk.Button(game_frame, text="AI Suggestion 🤖",
          font=("Arial", 12),
          bg="#ff9800",
          fg="white",
          command=suggest_move).pack(pady=10)

tk.Button(game_frame, text="Reset",
          font=("Arial", 12),
          bg="#f44336",
          fg="white",
          command=reset_game).pack(pady=5)

tk.Button(game_frame, text="Back to Menu",
          font=("Arial", 12),
          bg="#9c27b0",
          fg="white",
          command=back_to_menu).pack(pady=5)

# ------------------ START ------------------

root.mainloop()