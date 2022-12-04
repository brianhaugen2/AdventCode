//
// Created by brian on 12/2/21.
//
#include "algorithm"
#include "iostream"
#include "fstream"
#include "math.h"
#include "list"

using namespace std;

int main() {
    ifstream input_file;
    input_file.open(("2021/day3/input.txt"), ios::binary);
    int total_lines = count(istreambuf_iterator<char>(input_file), istreambuf_iterator<char>(), '\n') + 1;
    input_file.clear();
    input_file.seekg(0);
    string line;
    int i = 0;
    string input_data [total_lines];
    const int bit_len = 12;
    int zero[bit_len] = {};
    int one[bit_len] = {};
    string gamma = "";
    string epsilon = "";
    int part1_out;

    // Part 1
    while (getline(input_file, line)) {
        input_data[i] = line;
        for (int j=0; j < input_data[i].size(); j++) {
            string bit = line.substr(j, 1);
            if (bit == "0") {
                zero[j]++;
            } else one[j]++;
        }
        i++;
    }


    for (i=0; i < bit_len; i++) {
        if (zero[i] > one[i]) {
            gamma.append("0");
            epsilon.append("1");
        } else {
            gamma.append("1");
            epsilon.append("0");
        }
    }

    part1_out = stoi(gamma, nullptr, 2) * stoi(epsilon, nullptr, 2);
    cout << "Part 1: " << part1_out;

    // Part 2
    int oxygen_index [total_lines];
    int co2_index [total_lines];
    for (i=0; i<total_lines; i++) {
        oxygen_index[i] = i;
        co2_index[i] = i;
    }
    string oxygen_bit_criteria;
    string co2_bit_criteria;
    i = 0;
    while ((oxygen_index.size() > 1) || (i < bit_len)) {
        int zero = 0;
        int one = 0;
        for (int j=0; j<total_lines; j++) {
            if (input_data[j].substr(i, 1) == "0") {
                zero++;
            } else one++;
        }
        if (zero > one) {
            oxygen_bit_criteria = "0";
        } else oxygen_bit_criteria = "1";

        for (int j=0; j<total_lines; j++) {
            if oxygen_bit
        }
        while (k != oxygen_index.end()) {
            if (input_data[k])
        }
        i++;
    }




}
