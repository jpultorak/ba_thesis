from abc import ABC, abstractmethod
from typing import List

class InvalidMove(Exception):
    pass

class AbstractGame(ABC):

    def __init__(self):
        self.current_player = 1  #  Starting player. The other player is -1

    def switch_player(self) -> None:
        """Switch the turn to the other player."""
        self.current_player *= -1

    @abstractmethod
    def reset(self) -> None:
        """Reset the game to its initial state."""
        pass

    @abstractmethod
    def get_legal_moves(self) -> List[int]:
        """Return a list of all valid moves."""
        pass

    @abstractmethod
    def make_move(self, move: int) -> None:
        """Make a move and update the game state."""
        pass

    @abstractmethod
    def is_terminal(self) -> bool:
        """Return True if the game is finished."""
        pass

    @abstractmethod
    def evaluate(self) -> int | None:
        """Evaluate the game state.

        Return 1 for win, -1 for loss, 0 for draw, None for ongoing game.
        """
        pass
