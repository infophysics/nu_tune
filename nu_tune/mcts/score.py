"""
Tree and Playout score functions which are used to choose a parameter value,
and access a playout.
"""

class TreeScore:
    """
    Default class for Tree Scores
    'num_visits' and 'playout_scores'
    are the number of times a particular bin and its
    associated set of scores for each bin in the
    parameter range.
    """
    def __init__(self):
        pass

    def evaluate(self,
        num_visits,
        playout_scores
    ):
        pass

class PlayoutScore:
    """
    Default class for Playout scores
    'generated_values' will be the output of
    some generator, which could be just a list of four vectors,
    or some higher level deduced quantities.
    """
    def __init__(self):
        pass

    def evaluate(self,
        generated_values
    ):
        pass