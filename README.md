# Calculator Program

Welcome to the `calculator.py` program, a Python-based tool for evaluating simple mathematical expressions. This program employs infix-to-postfix conversion and expression trees to handle calculations. Below, you'll find an overview of the program, its components, and how to use it.

## Included Files

- `calculator.py`: The main program file responsible for evaluating mathematical expressions.
- `calculatorGUI.py`: A separate file that could be utilized for potential GUI-based interactions (not currently implemented).
- `stack.py`: A Python module used for managing a stack data structure.
- `tree.py`: A Python module for creating and evaluating expression trees.

## Program Workflow

Here's how the program operates:

1. The user provides a simple mathematical expression as input.
2. The program transforms the infix expression into postfix notation using the Shunting Yard algorithm.
3. An expression tree is constructed from the postfix notation.
4. The program evaluates the expression tree to calculate the result of the mathematical expression.
5. The result is then displayed to the user.

## How to Use

1. Run the program by executing `calculator.py` using a Python interpreter.

2. The program will greet you and prompt you to enter a mathematical expression.

3. To exit the calculator, input 'quit' or 'q' when prompted.

4. The program will evaluate the expression and show the result. You can continue entering expressions or exit as desired.

## Example Usage

Here's an example of how the program might be used:

```plaintext
Welcome to Calculator Program!
Please enter your expression here. To quit, enter 'quit' or 'q':
5 + 3 * (4 / 2)

The result of the expression is: 11.0

Please enter your expression here. To quit, enter 'quit' or 'q':
quit
Goodbye!
```

## Author Information

This program was crafted by Kriti Bhargava. 

## Acknowledgments

- The program leverages stack and tree data structures to handle mathematical expressions.

Please feel free to explore and improve this calculator program by submitting pull requests or reporting issues. Enjoy using the calculator!
