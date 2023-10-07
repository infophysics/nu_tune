"""
MCTS for neutrino generators.
"""
#	Required packages
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

from nu_tune.utils.logger import Logger
from nu_tune.generator.generator import Generator
from nu_tune.mcts.parameter import Parameter
from nu_tune.mcts.score import PlayoutScore

#	MIST class
class Tree:
    """
    Class for the mutual information search tree.
    """
    def __init__(self,
        parameters: list,
        generator:  Generator,
        score_function: PlayoutScore,
    ):
        self.logger = Logger("tree", output="both", file_mode="w")
        self.parameters = parameters
        self.generator = generator
        self.score_function = score_function
    
    def playout(self):
        bins = []
        parameter_values = []
        for parameter in self.parameters:
            bin, value = parameter.sample()
            bins.append(bin)
            parameter_values.append(value)
        generated_values = self.generator.generate(parameter_values)
        playout_score = self.score_function.evaluate(generated_values)
        self.backprop(bins, playout_score)

    def backprop(self,
        bins,
        playout_score
    ):
        for ii, parameter in enumerate(self.parameters):
            parameter.scores[bins[ii]].append(playout_score)