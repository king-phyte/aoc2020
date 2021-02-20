/*
--- Part Two ---

While it appears you validated the passwords correctly, they don't seem to be what the
Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job
at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character,
2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant
for the purposes of policy enforcement.

Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the policies?

*/
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include "../cppheaders/functions.hpp"

/**
The function checks whether a password is valid or not.
The validation is such that, the password must contain the character to be validated at least once in either of the positions specified.
If the above holds true, the function returns True. Else, it returns False.

@param pwd: str - The password to be validated.
@param char: Union[int, str] - The character to be used for validation.
@param first_position: int - Positon of character to be validated.
@param last_position: int - Position of character to be validated.
@return: bool
*/
bool is_valid(const std::string pwd, const char char_, const int first_position, const int last_position)
{
    if (pwd.find(char_) == pwd.npos)
    {
        return false;
    }
    if ((char_ == pwd[first_position - 1]) && (char_ != pwd[last_position - 1]))
    {
        return true;
    }
    else if ((char_ != pwd[first_position - 1]) && (char_ == pwd[last_position - 1]))
    {
        return true;
    }
    return false;
    
}


int find_number_of_valid_passwords(std::vector<std::string> data)
{
    int number_of_valid_passwords = 0;

    for (auto line : data)
    {
        std::vector<std::string> line_content = functions::split(line, " ");
        std::vector<std::string> min_and_max_occurence = functions::split(line_content[0], "-");
        int minimum_occurence = std::stoi(min_and_max_occurence[0]);
        int maximum_occurence = std::stoi(min_and_max_occurence[1]);
        char character_to_validate = line_content[1][0];
        std::string password = line_content[2];

        if (is_valid(password, character_to_validate
        , minimum_occurence, maximum_occurence))
        {
            ++number_of_valid_passwords;
        }
    }
    return number_of_valid_passwords;
}

int main()
{
    std::string line;
    std::vector<std::string> puzzle_input;
    std::ifstream f ("./input.txt");

    if (f.is_open())
    {
        while (getline(f, line))
        {
            puzzle_input.push_back(line);
        }
        
        f.close();
    }

    std::cout << find_number_of_valid_passwords(puzzle_input) << std::endl;  // Answer = 708

    return 0;
}

