import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import List


def read_input(input_fp: str) -> List[str]:
    with open(input_fp, "r") as f:
        lines = f.readlines()
    return lines


def main():
    input_fp = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_fp)

    # remove double spaces and new line characters
    lines = [line.replace("  ", " ").replace("\n", "") for line in lines]

    points = []
    matched = []
    for line in lines:
        _, score_card = line.split(":")[:2]
        score_card = score_card.strip()
        winning_nums, score_card_nums = score_card.split("|")[:2]
        winning_nums = winning_nums.strip().split(" ")
        score_card_nums = score_card_nums.strip().split(" ")
        matches = 0
        for num in winning_nums:
            if num in score_card_nums:
                matches += 1
        points.append(2 ** (matches - 1) if matches > 0 else 0)
        matched.append(matches)
    print(sum(points))

    scorecard_counts = [1] * len(lines)
    for i, match in enumerate(matched):
        for j in range(match):
            for k in range(scorecard_counts[i]):
                temp = i + j + 1
                if temp < len(scorecard_counts):
                    scorecard_counts[temp] += 1
    print(sum(scorecard_counts))

    
if __name__ == "__main__":
    main()
