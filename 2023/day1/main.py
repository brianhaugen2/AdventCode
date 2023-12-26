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


def parse_calibrate_value(line: str) -> int:
    # comment below line for part 1, uncomment for part 2
    line = convert_string_num_to_int(line)

    first_num = parse_first_number(line)
    last_num = parse_last_number(line)    
    return int(first_num + last_num)


def convert_string_num_to_int(line: str) -> int:
    string_to_num = {
        # "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five" : 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    line2 = ""
    for i in range(len(line)):
        if line[i].isnumeric():
            line2 += line[i]
        else:
            for k in string_to_num.keys():
                k_len = len(k)
                if k == line[i: i+k_len]:
                    line2 += str(string_to_num[k])
    return line2


def parse_first_number(line: str) -> str:
    for x in line:
        if x.isnumeric():
            return x
        

def parse_last_number(line: str) -> str:
    for x in reversed(line):
        if x.isnumeric():
            return x


def main():
    input_fp = os.path.join(os.path.dirname(__file__), "input.txt")

    # read the input file
    lines = read_input(input_fp)
    
    # get list of the numbers from the input file
    nums = [parse_calibrate_value(line) for line in lines]

    # get the sum of the numbers
    total = sum(nums)
    print(total)


if __name__ == "__main__":
    main()
