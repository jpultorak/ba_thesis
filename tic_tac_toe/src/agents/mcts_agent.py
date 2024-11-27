import math

from copy import deepcopy
from random import choice
from abc import ABC

from src.abstract_game import AbstractGame


class MctsNode(ABC):
    def __init__(self, game: AbstractGame, parent=None):
        self.game = game
        self.parent = parent
        self.children : dict[int, MctsNode]= {}
        self.visits = 0
        self.value = 0


    @staticmethod
    def selection_policy(node, parent_visits, exploration_weight: float):
        return node.value / node.visits + exploration_weight * math.sqrt(math.log(parent_visits) / node.visits)

    def best_child(self) -> "MctsNode":
        """Select the best child node using UCB."""
        # unvisited nodes have priority
        unvisited = [child for child in self.children.values() if child.visits == 0]
        if unvisited:
            return choice(unvisited)

        return max(
            self.children.values(),
            key=lambda child: MctsNode.selection_policy(child, self.visits, 1.41)
        )

    def select(self):
        """Find first node which is a leaf node"""
        node = self
        while node.children:
            node = node.best_child()

        if node.visits != 0:
            node.expand()
            return node.best_child()
        else:
            return node

    def expand(self) -> None:
        """Expand the node by adding ALL of its children"""
        for move in self.game.get_legal_moves():
            new_game = deepcopy(self.game)
            new_game.make_move(move)
            self.children[move] = MctsNode(new_game, parent=self)

    def simulate(self) -> int:
        """Simulate a random play-out from the current node."""
        simulation_game = deepcopy(self.game)
        while not simulation_game.is_terminal():
            move = choice(simulation_game.get_legal_moves())
            simulation_game.make_move(move)
        return simulation_game.evaluate()

    def backpropagate(self, result: int) -> None:
        """Update the node's value and visits based on the simulation result."""
        self.visits += 1
        if self.game.current_player == 1:
            self.value += result
        else:
            self.value -= result

        if self.parent:
            self.parent.backpropagate(result)  # Reverse result for the opponent

    def rollout(self, n: int) -> None:
        """Perform n rollouts"""
        for _ in range(n):
            sim_node = self.select()
            result = sim_node.simulate()
            sim_node.backpropagate(result)



