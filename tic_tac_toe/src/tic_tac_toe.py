from typing import List

from src.abstract_game import AbstractGame, InvalidMove


class TicTacToe(AbstractGame):


    # starting player: 1
    # second player: -1

    val_to_symbol = {1: "X", -1: "O", 0: " "}

    # [0, 1, 2]
    # [3, 4, 5]
    # [6, 7, 8]
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    def __init__(self) -> None:
        super().__init__()
        self.board = [0 for _ in range(9)]

    def reset(self) -> None:
        self.board = [0 for _ in range(9)]
        self.current_player = 1

    def display_board(self) -> None:
        for i in range(0, 9, 3):
            print('|'.join([TicTacToe.val_to_symbol[x] for x in self.board[i:i+3]]))
            if i < 6:
                print('-' * 5)
        print()

    def is_valid_move(self, position: int) -> bool:
        return position in range(0, 9) and not self.board[position]

    def make_move(self, move) -> None:
        if not self.is_valid_move(move):
            raise InvalidMove(f"Invalid move {move}")
        self.board[move] = self.current_player
        self.switch_player()

    def switch_player(self) -> None:
        self.current_player *= -1

    def get_legal_moves(self) -> List[int]:
        return [x for x in self.board if x != 0]

    def evaluate(self) -> int | None:
        for combo in TicTacToe.winning_combinations:
            combo_sum = sum(self.board[x] for x in combo)
            if combo_sum == 3:
                return 1
            elif combo_sum == -3:
                return -1
        if 0 not in self.board:
            return 0
        return None

    def is_draw(self) -> bool:
        return self.evaluate() == 0

    def is_terminal(self) -> bool:
        return self.evaluate() is not None

