from src.agents.base_agent import BaseAgent
from src.agents.random_agent import RandomAgent
from src.tic_tac_toe import TicTacToe


# simulate n games
def simulate(agent_1: BaseAgent, agent_2: BaseAgent, n):

    win_1, win_2, draws = 0, 0, 0
    agent_1_starts = True

    for i in range(n):
        game = TicTacToe()
        if not agent_1_starts:
            game.switch_player()

        agent_1_move = agent_1_starts

        while not game.is_terminal():
            if agent_1_move:
                move = agent_1.get_move(game)
            else:
                move = agent_2.get_move(game)
            game.make_move(move)

            winner = game.evaluate()
            if winner is not None:
                if winner == 1:
                    win_1 += 1
                elif winner == -1:
                    win_2 += 1
                elif winner == 0:
                    draws += 1
                agent_1_starts = not agent_1_starts
                continue

            agent_1_move = not agent_1_move

    return f"Out of {n} total games:\n" + f"Agent1 - {agent_1} won {win_1} ({100*win_1/n}%)\n"+ f"Agent2 - {agent_2} won {win_2} ({100*win_2/n}%)\n" + f"{draws} ({100*draws/n}%) draws"


if __name__ == '__main__':
    print(simulate(RandomAgent(1), RandomAgent(-1), 10000))