import os
import tkinter as tk
from tkinter import messagebox

# Основной класс игры
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-Нолики")
        self.current_player = "X"  # Начинает игрок "X"
        self.board = [""] * 9  # Игровое поле, представленное списком
        self.buttons = []  # Кнопки для игрового поля
        self.score = {"X": 0, "O": 0}  # Счет игроков
        self.create_board()
        self.create_scoreboard()

    # Создание игрового поля
    def create_board(self):
        for i in range(9):
            button = tk.Button(
                self.root, text="", font=("Arial", 24), width=5, height=2,
                command=lambda i=i: self.make_move(i)
            )
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5, sticky="nsew")
            self.buttons.append(button)

        for i in range(3):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    # Создание панели статистики
    def create_scoreboard(self):
        self.score_label = tk.Label(self.root, text=f"X: {self.score['X']} | O: {self.score['O']}", font=("Arial", 16))
        self.score_label.grid(row=3, column=0, columnspan=3)

    # Логика хода
    def make_move(self, index):
        if self.board[index] == "" and not self.check_winner():  # Если клетка пуста
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Победа!", f"Игрок {self.current_player} выиграл!")
                self.score[self.current_player] += 1
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Ничья", "Игра закончилась вничью!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
        self.update_scoreboard()

    # Обновление статистики
    def update_scoreboard(self):
        self.score_label.config(text=f"X: {self.score['X']} | O: {self.score['O']}")

    # Проверка победителя
    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Горизонтальные
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Вертикальные
            (0, 4, 8), (2, 4, 6)              # Диагонали
        ]
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ""):
                return True
        return False

    # Сброс игры
    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        for button in self.buttons:
            button.config(text="")

# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
