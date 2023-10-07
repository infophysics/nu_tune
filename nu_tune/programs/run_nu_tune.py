"""
Main program to run the nu_tune tree.
"""
from time import time
from datetime import datetime
import argparse
import os
os.environ["TQDM_NOTEBOOK"] = "false"

from nu_tune.dataset.dataset import Dataset
from nu_tune.generator.generator import Generator
from nu_tune.mcts.parameter import Parameter
from nu_tune.mcts.score import TreeScore, PlayoutScore
from nu_tune.mcts.tree import Tree
from nu_tune.nu_tune import nuTune
from nu_tune.utils.utils import *

def run():
    parser = argparse.ArgumentParser(
        prog='nu_tune runner',
        description='This program constructs a nu_tune MCTS',
        epilog='...'
    )
    parser.add_argument(
        '-n', dest='name', default='nu_tune',
        help='name for this run (default "nu_tune").'
    )
    parser.add_argument(
        '-scratch', dest='local_scratch', default='/local_scratch',
        help='location for the local scratch directory.'
    )
    parser.add_argument(
        '-data', dest='local_data', default='/local_data',
        help='location for the local data directory.'
    )
    args = parser.parse_args()
    nu_tune = nuTune(args)
    nu_tune.run()


if __name__ == "__main__":
    run()

