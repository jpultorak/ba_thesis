# BA thesis

**Ongoing** implementation of some cool stuff in python (might change)


---

## Project Structure

### `tic_tac_toe/`
- #### `src/agents/`
  - **`base_agent.py`**: Abstract base class for all agents.
  - **`random_agent.py`**: A baseline agent that plays random moves.
  - **`mcts_agent.py`**: An MCTS-based agent.
  - **`simulate.py`**: Framework for running simulations between agents.

- #### `src/mcts/`
  - **`abstract_game.py`**: Abstract class defining the game interface for MCTS.
  - **`mcts_node.py`**: Implementation of generic MCTS
  - **`tic_tac_toe.py`**: A sample implementation of the abstract game for Tic Tac Toe.
  
- #### `tests/` unit tests

---
