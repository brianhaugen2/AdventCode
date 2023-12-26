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


def main_part1():
    input_fp = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_fp)

    num_rows = len(lines)
    num_cols = len(lines[0]) - 1  # remove newline character

    part_numbers = []
    not_symbols = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in range(num_rows):
        j = 0
        while j < num_cols:
            # found a number
            if lines[i][j].isnumeric():
                # find how many digits in number
                digits_in_num = 0
                while lines[i][j + digits_in_num].isnumeric():
                    digits_in_num += 1

                # check if symbol is adjacent to number
                # stack the 3 rows into a single string
                temp_str = ""
                k_start = max(0, i - 1)
                k_end = min(num_rows, i + 2)
                for k in range(k_start, k_end):
                    l_start = max(0, j - 1)
                    l_end = min(num_cols, j + digits_in_num + 1)
                    temp_str += lines[k][l_start : l_end]
                    
                # check if symbol in temp_str
                for c in temp_str:
                    if c not in not_symbols:
                        part_num = int(lines[i][j : j + digits_in_num])
                        # print(part_num)
                        part_numbers.append(part_num)
                        break
                j += digits_in_num - 1
            j += 1
    print(sum(part_numbers))


def find_adjacent_numbers(line: str, l: int) -> int:
    temp_l_start = l
    while line[temp_l_start - 1].isnumeric():
        temp_l_start -= 1
    # find the end of the number
    temp_l_end = l
    while line[temp_l_end + 1].isnumeric():
        temp_l_end += 1
    return int(line[temp_l_start : temp_l_end + 1])


def main_part2():
    input_fp = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_fp)

    num_rows = len(lines)
    num_cols = len(lines[0]) - 1  # remove newline character

    gear_ratios = []

    for i in range(num_rows):
        for j in range(num_cols):
            # found a *
            if lines[i][j] == "*":
                # check if there are two numbers adjacent to *
                k_start = max(0, i - 1)
                k_end = min(num_rows, i + 2)
                l_start = max(0, j - 1)
                l_end = min(num_cols, j + 2)
                first_num = None
                second_num = None
                for k in range(k_start, k_end):
                    for l in range(l_start, l_end):
                        if lines[k][l].isnumeric():
                            found_num = find_adjacent_numbers(lines[k], l)
                            if first_num is None:
                                # find the start of the number
                                first_num = found_num
                            elif second_num is None and found_num != first_num:
                                second_num = found_num
                # get product of numbers if not None
                if first_num is not None and second_num is not None:
                    gear_ratios.append(first_num * second_num)
    print(sum(gear_ratios))


if __name__ == "__main__":
    main_part1()
    main_part2()
