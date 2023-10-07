"""
"""
from tqdm import tqdm

from nu_tune.utils.logger import Logger
from nu_tune.dataset.dataset import Dataset
from nu_tune.generator.generator import Generator
from nu_tune.mcts.parameter import Parameter
from nu_tune.mcts.score import TreeScore, PlayoutScore

class nuTune:
    """
    Main class for running a nuTune
    """
    def __init__(self,
        args
    ):
        self.logger = Logger("nu_tune", output="both", file_mode="w")
        self.args = args
        self.dataset = None
        self.parameters = None
        self.generator = None
        self.tree = None

    def run(self):
        self.logger.info("running nu_tune...")