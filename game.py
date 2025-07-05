import tkinter as tk
from tkinter import messagebox

def check_winner():
    global winner
    for combo in [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]:
        a, b, c = combo
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
            winner_symbol = buttons[a]["text"]
            for i in combo:
                buttons[i].config(
                    text=f"{buttons[i]['text']}",
                    font=("Helvetica", 28, "bold"),
                    fg="red"
                )
            winner = True
            root.after(300, lambda: messagebox.showinfo("Tic-Tac-Toe", f"🎉 Player {winner_symbol} wins! 🎉"))
            restart_button.grid(row=4, column=0, columnspan=3, pady=10)
            return

def check_draw():
    if all(btn["text"] != "" for btn in buttons) and not winner:
        root.after(300, lambda: messagebox.showinfo("Tic-Tac-Toe", "🤝 It's a Draw!"))
        restart_button.grid(row=4, column=0, columnspan=3, pady=10)

def button_click(index):
    global winner
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        buttons[index].config(fg="#000000")
        check_winner()
        check_draw()
        if not winner:
            toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"🔁 Player {current_player}'s Turn")

def restart_game():
    global current_player, winner
    for btn in buttons:
        btn.config(text="", font=("Helvetica", 24, "bold"))
    current_player = "X"
    winner = False
    label.config(text=f"🔁 Player {current_player}'s Turn")
    restart_button.grid_remove()

# === GUI Setup ===
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.configure(bg="#f0f0f0")
root.geometry("360x420")
root.resizable(False, False)

buttons = [tk.Button(
    root, text="", font=("Helvetica", 24, "bold"), width=5, height=2,
    bg="#FFFFFF", fg="#000000", relief="raised", bd=1,
    activebackground="#D3D3D3", cursor="hand2",
    command=lambda i=i: button_click(i)
) for i in range(9)]

for i, btn in enumerate(buttons):
    btn.grid(row=i // 3, column=i % 3, padx=4, pady=4)

label = tk.Label(root, text="🔁 Player X's Turn", font=("Helvetica", 16, "bold"),
                 bg="#f0f0f0", fg="#333333")
label.grid(row=3, column=0, columnspan=3, pady=(10, 0))

restart_button = tk.Button(
    root, text="🔄 Restart Game", font=("Helvetica", 14, "bold"),
    bg="#4CAF50", fg="#0c0b0b", activebackground="#45a049",
    padx=10, pady=5, cursor="hand2", command=restart_game
)
restart_button.grid(row=4, column=0, columnspan=3, pady=10)
restart_button.grid_remove()

# === Game State ===
current_player = "X"
winner = False

root.mainloop()
