# assignment: Programming Assignment 4
# author: Kriti Bhargava
# date: 03/06/2023
# file: calculator.py 
# input: The user will enter a simple mathmatical expression 
# output: The calculator will evaluate the function and output the answer. To quit the calculator you enter 'q' or 'quit'

import stack,tree 

# uses stack to transform infix to postfix.
def infix_to_postfix(infix):
    t_stack = stack.Stack()
    lst = []
    signs = ["^", "*", "/", "+", "-"]
    for i in infix:
        lst.append(i)
    num = ""
    operation = []
    for x in range(len(lst)):
        if lst[x].isnumeric() or lst[x] == ".":
            num += lst[x]
            
        else:
            if len(num) != 0:
                operation.append(num)
            num = ""
            operation.append(lst[x])
    if num != "":
        operation.append(num)
        num = ""
    lst = operation
    output = []

    for i in lst:
        if i.isnumeric() or "." in i:
            output.insert(len(output), i)
        elif i == "(":
            t_stack.push(i)
        elif i == ")":
            pop = ""
            while pop != "(":
                pop = t_stack.pop()
                if pop in signs:
                    output.append(pop)
        elif i in signs:
            while t_stack.size() != 0:
                nums = t_stack.peek()
                if nums in signs and signs.index(nums) <= signs.index(i):
                    s = t_stack.pop()
                    output.append(s)
                else:
                    break
            t_stack.push(i)
    while t_stack.size() != 0:
        s = t_stack.pop()
        if s in signs:
            output.append(s)
    z = ""
    for i in output:
        z += i + " "
    z = z[:-1]
    return z

#creates an expression tree, traverses it, and then returns the equation's value.
def calculate(infix):
    math_tree = tree.ExpTree(" ")
    math_tree = math_tree.make_tree(infix_to_postfix(infix))
    x = math_tree.evaluate(math_tree)
    return x

# takes user input(expression), iterates the expression through the calculator, and then returns the result.
if __name__ == '__main__':
    print(f'Welcome to Calculator Program!')

    while True:
        title = input("Please enter your expression here. To quit enter 'quit' or 'q':\n")
        if title == 'quit' or title == "q":
            print("Goodbye!")
            break
        else:
            print(calculate(title))
