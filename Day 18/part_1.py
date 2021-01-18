"""
--- Day 18: Operation Order ---

As you look out the window and notice a heavily-forested continent slowly appear over the horizon,
you are interrupted by the child sitting next to you. They're curious if you could help them with their math homework.

Unfortunately, it seems like this "math" follows different rules than you remember.

The homework (your puzzle input) consists of a series of expressions that consist of
addition (+), multiplication (*), and parentheses ((...)).
Just like normal math, parentheses indicate that the expression inside must be evaluated before it can be used
by the surrounding expression.
Addition still finds the sum of the numbers on both sides of the operator, and multiplication still finds the product.

However, the rules of operator precedence have changed. Rather than evaluating multiplication before addition,
the operators have the same precedence, and are evaluated left-to-right regardless of the order in which they appear.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
      9   + 4 * 5 + 6
         13   * 5 + 6
             65   + 6
                 71

Parentheses can override this order; for example, here is what happens if parentheses are added to form
1 + (2 * 3) + (4 * (5 + 6)):

1 + (2 * 3) + (4 * (5 + 6))
1 +    6    + (4 * (5 + 6))
     7      + (4 * (5 + 6))
     7      + (4 *   11   )
     7      +     44
            51

Here are a few more examples:

    2 * 3 + (4 * 5) becomes 26.
    5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 437.
    5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 12240.
    ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 13632.

Before you can help with the homework, you need to understand it yourself.
Evaluate the expression on each line of the homework; what is the sum of the resulting values?
"""
from io import StringIO
from simpleeval import simple_eval


def evaluate_addition(expression: str) -> int:
    return simple_eval(expression)


def evaluate_multiplication(expression: str) -> int:
    return simple_eval(expression)


def extract_bracket(expression: str) -> str:
    p = 0
    val = [StringIO(), []]

    for char in expression:
        if char == "(":
            p += 1
        if p:
            val[0].write(char)
        if char == ")" and p:
            p -= 1
        if not p and val[0].tell():
            val[1].append(val[0].getvalue())
            val[0] = StringIO()

    print(val[1][0])
    return val[1][0]


def evaluate_expression(expression: str) -> int:
    value_of_expression = ""
    index_of_current_char = 0
    while expression:
        if expression.isdigit():
            return int(value_of_expression)
        next_operand_index = index_of_current_char + 2
        next_operand = expression[next_operand_index]
        current_char = expression[index_of_current_char]

        if current_char == "+":
            if next_operand.isdigit():
                value_of_expression = evaluate_addition(expression[:next_operand_index + 1])
                print(value_of_expression)
                expression = str(value_of_expression) + expression[next_operand_index + 1:]
                index_of_current_char = 0

        elif current_char == "*":
            if next_operand.isdigit():
                value_of_expression = evaluate_multiplication(expression[:next_operand_index + 1])
                print(value_of_expression)
                expression = str(value_of_expression) + expression[next_operand_index + 1:]
                index_of_current_char = 0
        elif current_char == "(":
            print(extract_bracket(expression))

        index_of_current_char += 1

def main():
    # with open("./input.txt") as f:
    #     puzzle_input = [line.strip() for line in f.readlines()]
    with open("./test.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    sum_of_values = 0

    for line in puzzle_input:
        sum_of_values += evaluate_expression(line)

    print(sum_of_values)


if __name__ == '__main__':
    main()
