#include "algorithm"
#include "iostream"
#include "fstream"

using namespace std;

int main() {
    int part1_positive_count = 0;
    int part2_positive_count = 0;
    ifstream input_file ("2021/day1/input.txt");
    int total_count = count(istreambuf_iterator<char>(input_file), istreambuf_iterator<char>(), '\n');
    int input_data [total_count];
    input_file.clear();
    input_file.seekg(0);
    string line;


    if (input_file.is_open()) {
        int i = 0;
        while (getline(input_file, line)) {
            input_data[i] = stoi(line);
            // Part 1
            if (i > 0) {
                int diff = input_data[i] - input_data[i -1];
                if (diff > 0) {
                    part1_positive_count++;
                }
            }
            // Part 2
            if (i > 2) {
                int previous_sum = input_data[i-3] + input_data[i-3] + input_data[i-1];
                int current_sum = input_data[i-3] + input_data[i-1] + input_data[i];
                if ((current_sum - previous_sum) > 0){
                    part2_positive_count++;
                }

            }
            i++;
        }
        cout << "\nPart 1:\n" << part1_positive_count << " measurement larger than previous measurement\n";
        cout << "\nPart 2:\n" << part2_positive_count << " measurement larger than previous measurement\n";
    } else cout << "Unable to open file";

    return 0;
}