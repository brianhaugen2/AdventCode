import os
import re
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

    # red, blue, green
    threshold = {
        "red": 12, 
        "green": 13, 
        "blue": 14,
    }

    valid_games = []

    for line in lines:
        line = line.strip()
        game_num, game_sets = line.split(":")[:2]
        game_num = int(game_num[5:])
        valid = True
        for game_set in game_sets.split(";"):
            game_set_cube_count = {
                "red": 0,
                "blue": 0,
                "green": 0,
            }
            for color in game_set.split(","):
                cube_count = int(color.split(" ")[1])
                cube_color = color.split(" ")[2]
                game_set_cube_count[cube_color] += cube_count
            for color, count in game_set_cube_count.items():
                if count > threshold[color]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            valid_games.append(game_num)
    print(sum(valid_games))
    

def main_part2():
    input_fp = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_fp)

    game_product = []

    for line in lines:
        line = line.strip()
        game_num, game_sets = line.split(":")[:2]
        game_num = int(game_num[5:])
        game_cube_count = {
                "red": 0,
                "blue": 0,
                "green": 0,
            }
        for game_set in game_sets.split(";"):
            game_set_cube_count = {
                "red": 0,
                "blue": 0,
                "green": 0,
            }
            for color in game_set.split(","):
                cube_count = int(color.split(" ")[1])
                cube_color = color.split(" ")[2]
                game_set_cube_count[cube_color] += cube_count
            for color in game_set_cube_count.keys():
                if game_set_cube_count[color] > game_cube_count[color]:
                    game_cube_count[color] = game_set_cube_count[color]
        game_product.append(np.prod(list(game_cube_count.values())))
            
    print(sum(game_product))

if __name__ == "__main__":
    main_part1()
    main_part2()
