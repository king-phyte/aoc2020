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
from simpleeval import simple_eval


def evaluate_operation(expression: str) -> int:
    """
    Uses a "better" form of (built-in) eval (, security-wise) to evaluate an expression and return an integer
    """
    return simple_eval(expression)


def extract_bracket(expression: str) -> str:
    """
    Extracts and returns the contents of the first and outermost bracket.
    Examples:
        extract_bracket("2 + (3 * 4)") => 3 * 4
        extract_bracket("(1 + (2 + 3))") => 1 + (2 + 3))
    """
    level_within_bracket = 0
    expression_within_bracket = ""

    for char in expression[expression.index("("):]:
        if char == "(":
            level_within_bracket += 1
        if level_within_bracket:
            expression_within_bracket += char
        if char == ")" and level_within_bracket:
            level_within_bracket -= 1
        if not level_within_bracket:
            return expression_within_bracket[1:-1]  # Remove parentheses from expression with [1:-1]


def evaluate_expression(expression: str) -> int:
    """
    Evaluates an expression from left to right with no regard for precedence of some operators.
    Returns the value of the expression after evaluation
    """
    value_of_expression = ""
    index_of_current_char = 0
    while True:
        if expression.strip().isdigit():
            return int(expression)
        current_char = expression[index_of_current_char]
        next_operand_index = index_of_current_char + 2
        next_operand = expression[next_operand_index]

        if current_char in ("*", "+"):
            if next_operand.isdigit():
                value_of_expression = evaluate_operation(" ".join(expression.split()[:3]))
                expression = str(value_of_expression) + " " + " ".join(expression.split()[3:])
                index_of_current_char = 0
            elif next_operand == "(":
                expression_in_bracket = extract_bracket(expression)
                value_of_bracket_expression = evaluate_expression(expression_in_bracket)
                bracket_starts_from = next_operand_index
                bracket_ends_at = next_operand_index + len(expression_in_bracket) + 1
                expression = expression[:bracket_starts_from] \
                    + str(value_of_bracket_expression) \
                    + expression[bracket_ends_at + 1:]
                index_of_current_char = 0

        elif current_char == "(":
            expression_in_bracket = extract_bracket(expression)
            value_of_bracket_expression = evaluate_expression(expression_in_bracket)
            if expression.startswith("("):
                # If the expression starts with a (, the value of the expression must
                # replace the bracket accordingly (from the start)
                bracket_ends_at = len(expression_in_bracket) + 1
                expression = str(value_of_bracket_expression) + expression[bracket_ends_at + 1:]
            else:
                bracket_starts_from = next_operand_index
                bracket_ends_at = next_operand_index + len(expression_in_bracket) + 1
                expression = expression[:bracket_starts_from] \
                    + str(value_of_bracket_expression) \
                    + expression[bracket_ends_at + 1:]
            index_of_current_char = 0

        index_of_current_char += 1


def main():
    with open("./input.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    sum_of_values = 0

    for line in puzzle_input:
        sum_of_values += evaluate_expression(line)

    print(sum_of_values)  # Answer = 4_696_493_914_530


if __name__ == '__main__':
    main()
