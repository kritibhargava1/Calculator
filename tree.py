import math
from stack import Stack

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    def insertLeft(self,newNodeVal):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNodeVal)
        else:
            t = BinaryTree(newNodeVal)
            t.leftChild = self.leftChild
            self.leftChild = t
    
    def insertRight(self, newNodeVal):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNodeVal)
        else:
            t = BinaryTree(newNodeVal)
            t.rightChild = self.rightChild
            self.rightChild = t
    def getRightChild(self):
        if self.rightChild == None:
            return self.rightChild
        return self.rightChild
        
    def getLeftChild(self):
        return self.leftChild
    
    def getRootVal(self):
        return self.key
    
    def setRootVal(self, obj):
        self.key = obj
    def __str__(self):
        right_child = str(self.rightChild) if self.rightChild else ''
        left_child = str(self.leftChild) if self.leftChild else ''
        return str(self.key) + "[" + left_child + "]" + "[" + right_child + "]"
        #return  str(self.leftChild) + str(self.key) + str(self.rightChild)


class ExpTree (BinaryTree):
    def __init__(self, rootObj):
        super().__init__(rootObj)

    
    def make_tree(postfix):
        stack = Stack()
        operators = ['+', '-', '*', '/', '^']
        for symbol in postfix:
            if symbol not in operators:
                stack.push(ExpTree(symbol))
            else:
                x = ExpTree(symbol)
                x.rightChild = stack.pop()
                x.leftChild = stack.pop()
                stack.push(x)
        return stack.pop()


        
    def preorder(tree):
        s = ''
        if tree != None:
            s = tree.getRootVal()
            s += ExpTree.preorder(tree.getLeftChild())
            s += ExpTree.preorder(tree.getRightChild())
        return s

    def inorder(tree):
        s = ''
        if tree != None:
            if tree.getLeftChild() != None and tree.getRightChild() != None:
                s += '('
            s += ExpTree.inorder(tree.getLeftChild())
            s += tree.getRootVal()
            
            s += ExpTree.inorder(tree.getRightChild())
            if tree.getLeftChild() != None and tree.getRightChild() != None:
                s += ')'
        return s
    
    def postorder(tree):

        s = ''
        if tree != None:
            s += ExpTree.postorder(tree.getLeftChild())
            s += ExpTree.postorder(tree.getRightChild())
            s += tree.getRootVal()
        return s
    
    
    def evaluate(tree):

        operator = ["+", "/", "-", "*", "^"]
        if tree != None:
            
            if tree.getRootVal() in operator:
                a = ExpTree.evaluate(tree.getLeftChild())
                b = ExpTree.evaluate(tree.getRightChild())
                if tree.getRootVal() == "+":
                    return a + b
                elif tree.getRootVal() == "-":
                    return a - b
                elif tree.getRootVal() == "/":
                    return a / b
                elif tree.getRootVal() == "^":
                    return a ^ b
                elif tree.getRootVal() == "*":
                    return a * b
            else:
                if tree.getRootVal() == None:
                    return 0
                return float(tree.getRootVal())
            

    def __str__(self):
        return ExpTree.inorder(self)


if __name__ == '__main__':
    # test a BinaryTree

    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild() == None
    assert r.getRightChild() == None
    assert str(r) == 'a()()'

    r.insertLeft('b')
    print(r)
    print(r.getLeftChild().getRootVal())
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'

    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'

    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'

    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'

    # test an ExpTree

    postfix = '5 2 3 * +'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '(5+(2*3))'
    assert ExpTree.inorder(tree) == '(5+(2*3))'
    assert ExpTree.postorder(tree) == '523*+'
    assert ExpTree.preorder(tree) == '+5*23'
    assert ExpTree.evaluate(tree) == 11.0

    postfix = '5 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '((5+2)*3)'
    assert ExpTree.inorder(tree) == '((5+2)*3)'
    assert ExpTree.postorder(tree) == '52+3*'
    assert ExpTree.preorder(tree) == '*+523'
    assert ExpTree.evaluate(tree) == 21.0




    
