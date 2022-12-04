import os
import re
import sys
import json
from asammdf import MDF
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def complete_duplicated_work(row: pd.Series) -> bool:
    e1_start = row["Elf1_Start"]
    e1_stop = row["Elf1_Stop"]
    e2_start = row["Elf2_Start"]
    e2_stop = row["Elf2_Stop"]
    elf1_rng = range(e1_start, e1_stop + 1)
    elf2_rng = range(e2_start, e2_stop + 1)
    if (e1_start in elf2_rng) and (e1_stop in elf2_rng):
        return True
    elif (e2_start in elf1_rng) and (e2_stop in elf1_rng):
        return True
    else:
        return False

def partial_duplicated_work(row: pd.Series) -> bool:
    e1_start = row["Elf1_Start"]
    e1_stop = row["Elf1_Stop"]
    e2_start = row["Elf2_Start"]
    e2_stop = row["Elf2_Stop"]
    elf1_rng = range(e1_start, e1_stop + 1)
    elf2_rng = range(e2_start, e2_stop + 1)
    if (e1_start in elf2_rng) or (e1_stop in elf2_rng):
        return True
    elif (e2_start in elf1_rng) or (e2_stop in elf1_rng):
        return True
    else:
        return False


if __name__ == "__main__":
    df = pd.read_csv("input.txt", header=None)
    df.columns = ["Elf1", "Elf2"]
    # Part1
    df["Elf1_Start"] = [int(v.split("-")[0]) for v in df["Elf1"]]
    df["Elf1_Stop"] = [int(v.split("-")[1]) for v in df["Elf1"]]
    df["Elf2_Start"] = [int(v.split("-")[0]) for v in df["Elf2"]]
    df["Elf2_Stop"] = [int(v.split("-")[1]) for v in df["Elf2"]]
    df["complete_duplicated_work"] = df.apply(complete_duplicated_work, axis=1)
    print(df["complete_duplicated_work"].sum())
    # Part 2
    df["partial_duplicated_work"] = df.apply(partial_duplicated_work, axis=1)
    print(df["partial_duplicated_work"].sum())
