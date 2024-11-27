from abc import abstractmethod


class MCTSNode:


    def __init__(self, state):
        self.state = state
        self.parent = None
        self.result = 0
        self.total = 0

    def is_expanded(self):
        return self.total == 0

    @abstractmethod
    def is_terminal(self):
        pass

    @abstractmethod
    def generate_children(self):
        pass

    @abstractmethod
    def deepcopy(self):
        pass

    def best_child(self, exploration_weight=1.41):
        return max(
            self.children,
            key=lambda child: child.value / child.visits +
                              exploration_weight * math.sqrt(math.log(self.visits) / child.visits)
        )

    def select_leaf(self, f):
        cur_state : MCTSNode = self.deepcopy() # todo, figure out a better way to copy

        while not cur_state.is_terminal() or cur_state.is_expanded():
            nxt