from src.abstract_game import AbstractGame
from ..mcts.mcts_node import MctsNode  # Assuming you have MctsNode in a separate file
from .base_agent import BaseAgent  # Assuming BaseAgent is the parent class


class MCTSAgent(BaseAgent):
    def __init__(self, player_number, rollouts_per_turn):
        super().__init__(player_number)
        self.rollouts_per_turn = rollouts_per_turn

    def get_move(self, game: AbstractGame) -> int:
        root = MctsNode(game)
        root.rollout(self.rollouts_per_turn)

        UCT_vals = [(child, MctsNode.selection_policy(child, root.visits, 1.41)) for child in root.children.values()]
        # Select the move corresponding to the child with the highest visit count
        best_move, _ = max(
            root.children.items(),
            key=lambda move_child_pair: move_child_pair[1].visits
        )
        return best_move

    def __str__(self):
        return f"MCTSAgent{self.rollouts_per_turn}"
