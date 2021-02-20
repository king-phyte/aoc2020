#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

const int TARGET = 2020;

int find_target(const std::vector<int> numbers)
{
    for (int number : numbers)
    {
        int remainder = TARGET - number;
        if (std::find(numbers.begin(), numbers.end(), remainder) != numbers.end())
        {
            return remainder * number;
        }
    }
}

int main()
{
    std::vector<int> numbers;
    std::ifstream f ("./input.txt");
    std::string line;

    if (f.is_open())
    {
        while (getline(f, line))
        {
            numbers.push_back(std::stoi(line));
        }
        f.close();
    }

    std::cout << find_target(numbers); // Answer = 567171

    return 0;
}
