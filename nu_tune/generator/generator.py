"""
"""
from nu_tune.utils.logger import Logger

class Generator:
    """
    Wrapper for various neutrino event generators
    """
    def __init__(self):
        self.logger = Logger("generator", output="both", file_mode="w")

    def generate(self,
        parameter_values
    ):
        pass