from tkinter import *
from toegame import Move


class TicTacToeBoard(Tk):

    def __init__(self, game):
        super().__init__()
        self.display = None
        self.title("Tic-Toc Toe")
        self._cells = {}
        self._game = game
        self._create_menu()
        self.board_display()
        self.board_grid()

    def _create_menu(self):
        menu_bar = Menu(master=self)
        self.config(menu=menu_bar)
        file_menu = Menu(master=menu_bar)
        file_menu.add_command(label="Play Again", command=self.reset_board)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

    def reset_board(self):
        """reset the game's board to play again."""
        self._game.reset_game()
        self._update_display(msg="Are you ready?")
        for button in self._cells.keys():
            button.config(highlightbackground="lightblue", text="", fg="black")

    def board_display(self):
        display_frame = Frame(master=self)  # create a frame object
        display_frame.pack(fill=X)  # geometry manager to place the frame
        self.display = Label(master=display_frame, text="Are you ready?", font=("arial", 28, "bold"))
        self.display.pack()

    def board_grid(self):
        grid_frame = Frame(master=self)
        grid_frame.pack()

        for row in range(self._game.board_size):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=50)

            for col in range(self._game.board_size):
                button = Button(master=grid_frame, font=("arial", 35, "bold"),
                                fg="black", width=3, height=2, highlightbackground="lightblue")
                self._cells[button] = (row, col)
                button.bind("<ButtonPress-1>", self.play)
                button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    def _update_button(self, clicked_btn):
        clicked_btn.config(text=self._game.current_player.label)
        clicked_btn.config(fg=self._game.current_player.color)

    def _update_display(self, msg, color="black"):
        self.display["text"] = msg
        self.display["fg"] = color

    def _highlight_cells(self):
        for button, coordinates in self._cells.items():
            if coordinates in self._game.winner_combo:
                button.config(highlightbackground="red")

    def play(self, event):
        """handle a player's move."""
        clicked_btn = event.widget
        row, col = self._cells[clicked_btn]
        move = Move(row, col, self._game.current_player.label)
        if self._game.is_valid_move(move):
            self._update_button(clicked_btn)
            self._game.process_move(move)
            if self._game.is_tied():
                self._update_display(msg="Tied game!", color="red")
            elif self._game.has_winner():
                self._highlight_cells()
                msg = f'Player "{self._game.current_player.label}" won!'
                color = self._game.current_player.color
                self._update_display(msg, color)
            else:
                self._game.toggle_player()
                msg = f"{self._game.current_player.label}'s turn"
                color = self._game.current_player.color
                self._update_display(msg, color)

