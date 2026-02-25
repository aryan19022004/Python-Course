import tkinter as tk
import random

# ------------------ MAIN WINDOW ------------------
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("400x500")

board = [""] * 9
buttons = []
current_player = "X"
game_mode = None  # "2P" or "AI"

# ------------------ FUNCTIONS ------------------

def select_mode(mode):
    global game_mode
    game_mode = mode
    menu_frame.pack_forget()
    game_frame.pack()
    reset_game()

def click(index):
    global current_player

    if board[index] == "" and not check_winner():
        board[index] = current_player
        buttons[index].config(text=current_player)

        if check_winner():
            status_label.config(text=f"Player {current_player} Wins!")
            return
        elif "" not in board:
            status_label.config(text="It's a Draw!")
            return

        current_player = "O" if current_player == "X" else "X"
        status_label.config(text=f"Player {current_player}'s Turn")

        if game_mode == "AI" and current_player == "O":
            root.after(500, computer_move)

def computer_move():
    global current_player

    empty_indices = [i for i in range(9) if board[i] == ""]
    if empty_indices:
        move = random.choice(empty_indices)
        board[move] = "O"
        buttons[move].config(text="O")

        if check_winner():
            status_label.config(text="Computer Wins!")
            return
        elif "" not in board:
            status_label.config(text="It's a Draw!")
            return

        current_player = "X"
        status_label.config(text="Player X's Turn")

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
        btn.config(text="")

def back_to_menu():
    game_frame.pack_forget()
    menu_frame.pack()

# ------------------ MENU FRAME ------------------

menu_frame = tk.Frame(root)

tk.Label(menu_frame, text="Tic Tac Toe", font=("Arial", 24)).pack(pady=20)

tk.Button(menu_frame, text="2 Player Mode",
          font=("Arial", 14),
          command=lambda: select_mode("2P")).pack(pady=10)

tk.Button(menu_frame, text="Play With Computer",
          font=("Arial", 14),
          command=lambda: select_mode("AI")).pack(pady=10)

menu_frame.pack()

# ------------------ GAME FRAME ------------------

game_frame = tk.Frame(root)

status_label = tk.Label(game_frame, text="Player X's Turn",
                        font=("Arial", 14))
status_label.pack(pady=10)

board_frame = tk.Frame(game_frame)
board_frame.pack()

for i in range(9):
    btn = tk.Button(board_frame, text="", font=("Arial", 20),
                    width=5, height=2,
                    command=lambda i=i: click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

tk.Button(game_frame, text="Reset",
          font=("Arial", 12),
          command=reset_game).pack(pady=10)

tk.Button(game_frame, text="Back to Menu",
          font=("Arial", 12),
          command=back_to_menu).pack(pady=5)

# ------------------ START ------------------

root.mainloop()