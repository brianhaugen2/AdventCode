import os
import re
import sys
import json
from asammdf import MDF
import numpy as np
import pandas as pd
from typing import Tuple
import matplotlib.pyplot as plt

def rock_paper_scissors_verdict(row: pd.Series) -> pd.Series:
    opp, self  = row["Opponent"], row["Self"]
    # opp chose rock
    if opp == "A":
        # self chose rock, tie
        if self == "X":
            row["Opponent_Score"] = 1 + 3
            row["Self_Score"] = 1 + 3
        # self chose paper, self wins
        elif self == "Y":
            row["Opponent_Score"] = 1 + 0
            row["Self_Score"] = 2 + 6
        # self chose scissors, opp wins
        elif self == "Z":
            row["Opponent_Score"] = 1 + 6
            row["Self_Score"] = 3 + 0
    # opp chose paper
    elif opp == "B":
        # self chose rock, opp wins
        if self == "X":
            row["Opponent_Score"] = 2 + 6
            row["Self_Score"] = 1 + 0
        # self chose paper, tie
        elif self == "Y":
            row["Opponent_Score"] = 2 + 3
            row["Self_Score"] = 2 + 3
        # self chose scissors, self wins
        elif self == "Z":
            row["Opponent_Score"] = 2 + 0
            row["Self_Score"] = 3 + 6
    # opp chose scissors
    elif opp == "C":
        # self chose rock, self wins
        if self == "X":
            row["Opponent_Score"] = 3 + 0
            row["Self_Score"] = 1 + 6
        # self chose paper, opp wins
        elif self == "Y":
            row["Opponent_Score"] = 3 + 6
            row["Self_Score"] = 2 + 0
        # self chose scissors, tie
        elif self == "Z":
            row["Opponent_Score"] = 3 + 3
            row["Self_Score"] = 3 + 3
    return row


def reverse_rock_paper_scissors_for_self(row: pd.Series) -> pd.Series:
    opp = row["Opponent"]
    self = row["Self"]
    # opp chose rock
    if opp == "A":
        # need to lose, self chose scissors
        if self == "X":
            row["Self"] = "Z"
        # need to tie, self chose rock
        elif self == "Y":
            row["Self"] = "X"
        # need to win, self chose paper
        elif self == "Z":
            row["Self"] = "Y"
    # opp chose paper
    elif opp == "B":
        # need to lose, self chose rock
        if self == "X":
            row["Self"] = "X"
        # need to tie, self chose paper
        elif self == "Y":
            row["Self"] = "Y"
        # need to win, self chose scissors
        elif self == "Z":
            row["Self"] = "Z"
    # opp chose scissors
    elif opp == "C":
        # need to lose, self chose paper
        if self == "X":
            row["Self"] = "Y"
        # need to tie, self chose scissors
        elif self == "Y":
            row["Self"] = "Z"
        # need to win, self chose rock
        elif self == "Z":
            row["Self"] = "X"
    return row


if __name__ == "__main__":
    # Part 1
    # read data
    df = pd.read_csv("input.txt", sep=" ", header=None)
    df.columns = ["Opponent", "Self"]

    df = df.apply(rock_paper_scissors_verdict, axis=1)
    print(df["Self_Score"].sum())

    # Part 2
    df = df.apply(reverse_rock_paper_scissors_for_self, axis=1)
    df = df.apply(rock_paper_scissors_verdict, axis=1)
    print(df["Self_Score"].sum())
