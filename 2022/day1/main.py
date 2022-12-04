if __name__ == "__main__":
    # PART 1
    with open("input.txt", "r") as f:
        input = f.read()

    # split list into calories per item for each elf
    elves_items = sorted([sum([int(i) for i in e.split("\n")]) for e in input.split("\n\n")], reverse=True)
    # find the max calories for each elf
    print(elves_items[0])

    # PART 2
    print(sum(elves_items[:3]))
