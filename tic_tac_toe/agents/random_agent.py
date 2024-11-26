import random
from .base_agent import BaseAgent

class RandomAgent(BaseAgent):
    def __init__(self, player_number):
        super().__init__(player_number)

    def get_move(self, game):
        valid_moves = [i for i in range(9) if game.is_valid_move(i)]
        return random.choice(valid_moves)

    def __str__(self):
        return "RandomAgent"
