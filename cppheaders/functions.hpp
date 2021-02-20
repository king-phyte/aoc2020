#ifndef FUNCTIONS_HPP
#define FUNCTIONS_HPP
#include <vector>
#include <string>

namespace functions
{
    template <typename T>
    void print(const std::vector<T> list);

    int count(std::string str, const std::string value);
    int count(std::string str, const char value);

    std::vector<std::string> split(std::string str, const std::string delimeter);
} // namespace functions

#endif
