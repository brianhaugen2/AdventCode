import os
import re
import sys
import json
from asammdf import MDF
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def str_to_priority(c: str) -> int:
    return ord(c) - 96 if ord(c) > 96 else ord(c) - 38


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
    # Part 1
    priority = []
    for line in lines:
        half_line = int(len(line) / 2)
        for c in line[:half_line]:
            if c in line[half_line:]:
                priority.append(str_to_priority(c))
                break
    print(sum(priority))
    # Part 2
    second = []
    for i in range(int(len(lines) / 3)):
        found = False
        for c in lines[i * 3]:
            if (c in lines[(i * 3) + 1]) and (c in lines[(i * 3) + 2]):
                second.append(str_to_priority(c))
                break
    print(sum(second))
