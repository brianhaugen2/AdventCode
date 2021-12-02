//
// Created by brian on 12/2/21.
//
#include "algorithm"
#include "iostream"
#include "fstream"

using namespace std;

int main() {
    ifstream input_file ("2021/day2/input.txt");
    int total_lines = count(istreambuf_iterator<char>(input_file), istreambuf_iterator<char>(), '\n') + 1;
    input_file.clear();
    input_file.seekg(0);
    string line;
    int i = 0;
    string input_data [total_lines];
    int depth = 0;
    int horizontal = 0;
    string direction;
    int steps;

    // Part 1
    while (getline(input_file, line)) {
        input_data[i] = line;
        direction = line.substr(0, line.find(" "));
        steps = stoi(line.substr(direction.size(), line.find(" ")));
        if (direction == "up") {
            depth -= steps;
        } else if (direction == "down") {
            depth += steps;
        } else if (direction == "forward") {
            horizontal += steps;
        } else return -1;
        i++;
    }
    int part1_out = horizontal * depth;
    cout << "Part 1: " << part1_out << "\n";

    // Part 2
    horizontal = 0;
    depth = 0;
    int aim = 0;
    for (i = 0; i < total_lines; i++) {
        line = input_data[i];
        direction = line.substr(0, line.find(" "));
        steps = stoi(line.substr(direction.size(), line.find(" ")));
        if (direction == "up") {
            aim -= steps;
        } else if (direction == "down") {
            aim += steps;
        } else if (direction == "forward") {
            horizontal += steps;
            depth += (aim * steps);
        } else return -1;
    }
    int part2_out = horizontal * depth;
    cout << "Part 2: " << part2_out << "\n";
}

