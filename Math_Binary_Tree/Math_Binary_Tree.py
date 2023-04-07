#!/bin/python3

import math
import os
import random
import re
import sys
import operator
def makeTree(root,trl,trr):
    return ['btree', root,trl,trr]

def make_empty_tree():
    return ['btree']

def is_btree(tree):
    if tree[0] == "btree":
        return True
    else:
        return False
    
def root(tree):
    return tree[1]

def left_subtree(tree):
    return tree[2]

def right_subtree(tree):
    return tree[3]

def is_empty_tree(tree):
    if tree == ['btree']:
        return True
    return False

def is_leaf_tree(tree):
    return is_empty_tree(left_subtree(tree)) and is_empty_tree(right_subtree(tree))

def preorder(tree):
    if is_empty_tree(tree):
        return []
    else:
        return [root(tree)]+preorder(left_subtree(tree))+preorder(right_subtree(tree))

def inorder(tree):
    if is_empty_tree(tree):
        return []
    else:
        return inorder(left_subtree(tree))+[root(tree)]+inorder(right_subtree(tree))

#
# Include the 'postorder' function (from PROBLEM 1) below.
#

# question 1
def postorder(tree):
    if is_btree(tree):
        if is_empty_tree(tree):
            return []
        else:
            return postorder(left_subtree(tree)) + postorder(right_subtree(tree)) + [root(tree)]




# question 2
def stack():
    return ("stack", [])


def contents(stack):
    return stack[1]


def top(stack):
    if is_stack(stack) and not stack_empty(stack):
        return contents(stack)[-1]


def is_stack(stack):
    return type(stack) == tuple and stack[0] == 'stack' and type(contents(stack)) == list and len(stack) == 2


def stack_empty(stack):
    return contents(stack) == []


def push(stack, el):
    if is_stack(stack) :
        contents(stack).append(el)
    else: raise 'push'


def pop(stack):
    if is_stack(stack) and not stack_empty(stack):
        contents(stack).pop(-1)





def is_operator(operation):
    if operation in ['-', '+', '*', '/']:
        return True
    return False


def apply_operator(operat, num2, num1):

    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    op_func = ops[operat]
    result = op_func(num2, num1)

    return result




def evalPostfix(tree):
    if is_btree(tree) and not is_empty_tree(tree):
        list_post = postorder(tree)
        stac = stack()
        print(list_post)
        for i in list_post:
            if not is_operator(i):
                push(stac, i)
            else:
                num1 = top(stac)
                pop(stac)
                num2 = top(stac)
                pop(stac)
                push(stac, apply_operator(i, num2, num1))
        return top(stac)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    nodes = [None] * (n+1)
    nodes[0] = make_empty_tree()
    for i in range(n):
        i, v, l, r = input().strip().split(' ')
        if v.isdigit():
           v = int(v)
        i, l, r = int(i), int(l), int(r)
        
        nodes[i] = makeTree(v, nodes[l], nodes[r])

    if n > 0:
        answer = evalPostfix(nodes[1])
    else:
        answer = 0

    fptr.write(str(answer) + '\n')

    fptr.close()
