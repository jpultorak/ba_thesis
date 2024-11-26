from random import random

from game import TicTacToe
from agents.random_agent import RandomAgent
import random

def main():
    game = TicTacToe()
    player_symbol = random.choice([1, -1])
    agent_symbol = (-1)*player_symbol
    agent = RandomAgent(agent_symbol)

    print("Time to play some Tic Tac Toe bruv")
    game.display_board()

    while True:
        if game.current_player == player_symbol:
            move = int(input("Enter your move (1-9): ")) - 1
            while not game.is_valid_move(move):
                move = int(input("Incorrect move! Enter your move (1-9): ")) - 1

        else:
            print("Agent is making a move...")
            move = agent.get_move(game)

        assert game.is_valid_move(move)
        game.make_move(move)
        game.display_board()

        winner = game.check_winner()
        if winner is not None:
            if winner == player_symbol:
                print("Player wins!")
            elif winner == agent_symbol:
                print("Agent wins")
            else:
                print("It's a draw!")
            break



if __name__ == "__main__":
    main()
