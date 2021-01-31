"""
--- Part Two ---

You manage to answer the child's questions and they finish part 1 of their homework
but get stuck when they reach the next section: advanced math.

Now, addition and multiplication have different precedence levels, but they're not the ones you're familiar with.
Instead, addition is evaluated before multiplication.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are now as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
  3   *   7   * 5 + 6
  3   *   7   *  11
     21       *  11
         231

Here are the other examples from above:

    1 + (2 * 3) + (4 * (5 + 6)) still becomes 51.
    2 * 3 + (4 * 5) becomes 46.
    5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 1445.
    5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 669060.
    ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 23340.

What do you get if you add up the results of evaluating the homework problems using these new rules?

"""
from part_1 import evaluate_operation, extract_bracket
import part_1

ADDITION_OPERATOR = "+"


def evaluate_expression(expression: str) -> int:
    """
    1 + 2 * 3 + 4 * 5 + 6
    1 + (2 * 3) + (4 * (5 + 6))
    2 * 3 + (4 * 5)
    5 + (8 * 3 + 9 + 3 * 4 * 3)
    5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
    ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
    Check if "+" is in expression
        If none is in the expression
            Evaluate the expression and return the answer
        Else
            Find the first "+"
            Obtain the left and right operands
            Evaluate them and replace the section of the operation with the value of the operation
    """

    while ADDITION_OPERATOR in expression:
        print(f"Before => {expression}")
        expression = expression.split()

        addition_operator_index = expression.index(ADDITION_OPERATOR)
        left_operand_index = addition_operator_index - 1
        right_operand_index = addition_operator_index + 1
        left_operand = expression[left_operand_index]
        right_operand = expression[right_operand_index]

        if expression[0].startswith("("):
            bracket = extract_bracket(" ".join(expression))
            value_of_expression = evaluate_expression(bracket)
            expression = str(value_of_expression) + " " + " ".join(expression[len(bracket.split()):])
            print(f"After => {expression}")

        elif left_operand.isdigit() and right_operand.isdigit():
            value_of_expression = evaluate_operation(f"{left_operand} + {right_operand}")
            expression = " ".join(expression[:left_operand_index]) \
                         + " " + str(value_of_expression) + " " \
                         + " ".join(expression[right_operand_index + 1:])
            expression = expression.strip()
            print(f"After => {expression}")

        elif left_operand.isdigit() and right_operand.startswith("("):
            """
            Extract the bracket to the right, evaluate it and return the result
            """
            to_right = " ".join(expression[right_operand_index:])
            bracket_to_right = extract_bracket(to_right)
            result_of_bracket = evaluate_expression(bracket_to_right)
            value_of_expression = evaluate_operation(f"{left_operand} + {result_of_bracket}")

            if to_right[len(bracket_to_right.split())].endswith("))"):
                print("Yes")
                expression = " ".join(expression[:left_operand_index]) \
                             + " " + str(value_of_expression) + ") " \
                             + " ".join(expression[right_operand_index + len(bracket_to_right.split()):])
            else:

                print("No")
                expression = " ".join(expression[:left_operand_index]) \
                             + " " + str(value_of_expression) + " " \
                             + " ".join(expression[right_operand_index + len(bracket_to_right.split()):])
            expression = expression.strip()

            print(f"After => {expression}")

        elif left_operand.endswith(")") and right_operand.isdigit():
            last_bracket_index: int
            for index, item in enumerate(expression):
                if item.startswith("("):
                    last_bracket_index = index
            value = extract_bracket(" ".join(expression[last_bracket_index:]))
            som = evaluate_expression(value)
            expression = " ".join(expression[:left_operand_index - len(value.split()) + 1]) \
                         + " " + str(som) + " " \
                         + " ".join(expression[addition_operator_index:])
            print(f"After => {expression}")

        elif left_operand.startswith("(") and right_operand.startswith("("):
            bracket = extract_bracket(" ".join(expression[left_operand_index:]))
            value_of_expression = evaluate_expression(bracket)
            expression = " ".join(expression[:left_operand_index]) \
                         + " " + str(value_of_expression) + " " \
                         + " ".join(expression[left_operand_index + len(bracket.split()):])
            print(f"After => {expression}")

        elif left_operand.endswith(")") and right_operand.startswith("("):
            last_bracket_index: int
            for index, item in enumerate(expression):
                if item.startswith("("):
                    last_bracket_index = index

            left = extract_bracket(" ".join(expression[last_bracket_index:]))
            right = extract_bracket(" ".join(expression[right_operand_index:]))
            value_of_expression = evaluate_expression(f"{left} + {right}")
            expression = " ".join(expression[:left_operand_index - len(left.split()) + 1]) \
                         + " " + str(value_of_expression) + " " \
                         + " ".join(expression[right_operand_index + len(right.split()):])
            print(f"After => {expression}")

        elif left_operand.isdigit() and right_operand.endswith(")"):
            detailed_right_operand = list(right_operand)
            digits = "".join([x for x in detailed_right_operand if x.isdigit()])
            brackets = "".join([x for x in detailed_right_operand if not x.isdigit()])
            value_of_expression = evaluate_operation(f"{left_operand} + {digits}")
            expression = " ".join(expression[:left_operand_index]) \
                         + " " + str(value_of_expression) + f"{brackets} "  \
                         + " ".join(expression[right_operand_index + 1:])

        elif left_operand.startswith("(") and right_operand.endswith(")"):
            if left_operand.startswith("(("):
                bracket = extract_bracket(" ".join(expression[left_operand_index:right_operand_index + 1])[1:])
            else:
                bracket = extract_bracket(" ".join(expression[left_operand_index:right_operand_index + 1]))
            result_of_bracket = evaluate_expression(bracket)
            expression = " ".join(expression[:left_operand_index]) \
                         + " " + str(result_of_bracket) + " " \
                         + " ".join(expression[right_operand_index + 1:])
            expression = expression.strip()

            if left_operand.startswith("(("):
                expression = "(" + expression

            print(f"After => {expression}")

        elif left_operand.startswith("(") and right_operand.isdigit():
            detailed_left_operand = list(left_operand)
            digits = "".join([x for x in detailed_left_operand if x.isdigit()])
            brackets = "".join([x for x in detailed_left_operand if not x.isdigit()])
            value_of_expression = evaluate_operation(f"{digits} + {right_operand}")
            expression = " ".join(expression[:left_operand_index]) \
                         + f" {brackets}" + str(value_of_expression) + " " \
                         + " ".join(expression[right_operand_index + 1:])
            expression = expression.strip()
            print(f"After => {expression}")

    return part_1.evaluate_expression(expression)


def main():
    with open("./input.txt") as f:
        puzzle_input = f.readlines()

    with open("./test.txt") as f:
        puzzle_input = f.readlines()

    for line in puzzle_input:
        print(evaluate_expression(line.strip()))

    # sum_of_values = 0

    # for line in puzzle_input:
    #     sum_of_values += evaluate_expression(line.strip())
    #
    # print(sum_of_values)


if __name__ == '__main__':
    main()
