from tkinter import *
import stack
import tree

#creates an expression tree, traverses it, and then returns the equation's value.
def calculate(infix):
    math_tree = tree.ExpTree(" ")
    math_tree = math_tree.make_tree(infix_to_postfix(infix))
    x = math_tree.evaluate(math_tree)
    return x

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

def calculator(gui):
    # name the gui window
    gui.title("Calculator")
    # make a entry text box
    entrybox = Entry(gui, width=36, borderwidth=5)
    # position the entry text box in the gui window using the grid manager
    entrybox.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # create buttons: 1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,=
    b0 = addButton(gui, entrybox, '0')
    b1 = addButton(gui, entrybox, '1')
    b2 = addButton(gui, entrybox, '2')
    b3 = addButton(gui, entrybox, '3')
    b4 = addButton(gui, entrybox, '4')
    b5 = addButton(gui, entrybox, '5')
    b6 = addButton(gui, entrybox, '6')
    b7 = addButton(gui, entrybox, '7')
    b8 = addButton(gui, entrybox, '8')
    b9 = addButton(gui, entrybox, '9')
    b_add = addButton(gui, entrybox, '+')
    b_sub = addButton(gui, entrybox, '-')
    b_mult = addButton(gui, entrybox, '*')
    b_div = addButton(gui, entrybox, '/')
    b_clr = addButton(gui, entrybox, 'c')
    b_eq = addButton(gui, entrybox, '=')

    # add buttons to the grid
    buttons = [b7, b8, b9, b_clr,
               b4, b5, b6, b_sub,
               b1, b2, b3, b_add,
               b_mult, b0, b_div, b_eq]
    k = 4
    for i in range(k):
        for j in range(k):
            buttons[i*k+j].grid(row=i + 1, column=j, columnspan=1)


def addButton(gui, entrybox, value):
    return Button(gui, text=value, height=4, width=9, command=lambda: clickButton(entrybox, value))

#the buttons are 
def clickButton(entrybox, value):
    if value == "c":
        clear_box(entrybox)
        
    elif value == "=":
        calc = entrybox.get()
        clear_box(entrybox)
        entrybox.insert(0, calculate(calc))
    else:
        entrybox.insert(len(entrybox.get()), value)

#Clears the entry box for next expression
def clear_box(entrybox):
    for i in range(len(entrybox.get())):
        entrybox.delete(0, 1)

# main program
# create the main window
gui = Tk()
# create the calculator layout
calculator(gui)
# update the window
gui.mainloop()
