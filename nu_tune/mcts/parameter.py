"""
Class for describing a parameter in the neutrino generator,
which is binned and sampled during a MCTS playout.
"""
import numpy as np

from nu_tune.mcts.score import TreeScore

class Parameter:
    """
    """
    def __init__(self,
        name:   str="",
        num_bins:   int=10,
        var_range:  list=[0.0,1.0],
        discrete:   bool=False,
        score_function: TreeScore=None
    ):
        self.name = name
        self.bins = np.array([ii for ii in range(num_bins)])
        self.var_range = var_range
        self.discrete = discrete
        if not self.discrete:
            total_range = self.var_range[1] - self.var_range[0]
            bin_width = total_range / float(num_bins)
            self.bin_left = np.array([
                self.var_range[0] + ii * bin_width 
                for ii in range(num_bins)
            ])
            self.bin_right = np.array([
                self.var_range[0] + (ii + 1) * bin_width 
                for ii in range(num_bins)
            ])
        self.num_visits = np.array([0 for ii in range(num_bins)])
        self.playout_scores = [[] for ii in range(num_bins)]

        self.score_function = score_function
    
    def evaluate(self):
        tree_scores = self.score_function.evaluate(
            self.num_visits,
            self.playout_scores
        )
        return tree_scores
    
    def sample_bin(self,
        bin:    int=0
    ):
        self.num_visits[bin] += 1
        if not self.discrete:
            return bin, np.random.uniform(
                self.bin_left[bin],
                self.bin_right[bin],
                1
            )
        else:
            return bin, self.var_range[bin]
    
    def sample(self):
        """
        There are two basic situations, either 
            (1) not all bins have been visited:
                throw a random number to decide
                which of the bins that are left need
                to be visited.
            (2) if all bins have been visited at least
                once, then use the score to choose which
                bin to visit.
        """
        # check is any bins have not been visited 
        if 0 in self.num_visits:
            un_visited = self.bins[(self.num_visits == 0)]
            np.random.shuffle(un_visited)
            return self.sample_bin(un_visited[0])
        else:
            tree_scores = self.evaluate()
            max_bin = np.argmax(tree_scores)
            return self.sample_bin(max_bin)
