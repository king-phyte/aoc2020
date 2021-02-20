#include "./functions.hpp"
#include <iostream>

int functions::count(std::string str, const std::string value)
{
    int number = 0;

    do
    {
        if ((str.find(value)) == str.npos)
        {
            return number;
        }

        int pos = str.find(value);
        ++number;
        str = str.substr(pos + 1);
    } while (true);
    return number;
}

int functions::count(std::string str, const char value)
{
    int number = 0;

    do
    {
        if ((str.find(value)) == str.npos)
        {
            return number;
        }

        int pos = str.find(value);
        ++number;
        str = str.substr(pos + 1);
    } while (true);
    return number;
}

std::vector<std::string> functions::split(std::string str, const std::string delimeter = " ")
{
    std::vector<std::string> results;

    while (true)
    {

        if (str.find(delimeter) == str.npos)
        {
            results.push_back(str);
            return results;
        }
        else
        {
            std::string buffer = "";
            for (int i = 0; i < str.find(delimeter); i++)
            {
                buffer += str[i];
            }
            if (!buffer.empty())
            {
                results.push_back(buffer);
                std::string new_string = "";

                for (int j = str.find(delimeter) + 1; j < (str.length()) ; j++)
                {
                    new_string += str[j];
                }
                str = new_string;
            }
        }
    }
}


template <typename T>
void functions::print(const std::vector<T> list)
{
    std::cout << "[";
    for (auto item: list)
    {
        std::cout << "\"" << item << "\"";

        if (!(item == list.back()))
        {
            std::cout << ", ";
        }
    }
    std::cout << "]\n";
}
