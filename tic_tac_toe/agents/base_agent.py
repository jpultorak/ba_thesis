class BaseAgent:
    def __init__(self, player_number: int):
        self.player_number = player_number

    def get_move(self, game):
        raise NotImplementedError("This method should be implemented by subclasses.")

    def __str__(self) -> str:
        return f"Base agent"
