#include <iostream>
#include <fstream>
#include <string>
#include <vector>

const int TARGET = 2020;

int find_target(const std::vector<int> numbers)
{
    int index_of_second_number = 0, index_of_third_number = 1;

    for (int number : numbers)
    {
        while (index_of_second_number < numbers.size())
        {
            while (index_of_third_number < numbers.size())
            {
                int second_number = numbers[index_of_second_number];
                int third_number = numbers[index_of_third_number];
                int sum = number + second_number + third_number;

                if (sum == TARGET)
                {
                    return number * numbers[index_of_second_number] * numbers[index_of_third_number];
                }
                ++index_of_third_number;
            }
            ++index_of_second_number;
            index_of_third_number = 1;
        }
        index_of_second_number = 0;
    }
}

int main()
{
    std::ifstream f("./input.txt");
    std::vector<int> numbers;
    std::string line;

    while (getline(f, line))
    {
        numbers.push_back(std::stoi(line));
    }

    std::cout << find_target(numbers) << std::endl;  // Answer = 212_428_694

    return 0;
}
