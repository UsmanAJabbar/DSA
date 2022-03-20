#!/usr/bin/env python3
"""Valid Parenthesis"""


def validParenthesis(s: str) -> bool:
    """
    -----------------
    Valid Parenthesis
    -----------------
    Given a string s containing just the characters
    '(', ')', '{', '}', '[' and ']', determine if the input
    string is valid.

    An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
    """

    tags = {
        '{': '}',
        '[': ']',
        '(': ')'
    }

    stack = []

    for char in s:
        # If char is an opening tag, append to the stack
        if char in tags:
            stack.append(char)
        # Else, check if the closing tag is a value of char
        elif stack and tags[stack[-1]] == char:
            stack.pop()
        else:
            return False
    
    return stack == []
