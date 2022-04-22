def balanced_parenthesis(s: str) -> str:
    """Given a string s of '(' , ')' and lowercase English characters.

    Your task is to remove the minimum number of parentheses
    ( '(' or ')', in any positions ) so that the resulting
    parentheses string is valid and return any valid string.

    Formally, a parentheses string is valid if and only if:

    It is the empty string, contains only lowercase characters, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.

    Args:
        s (str): input string

    Returns:
        str: Cleaned up string with the invalid parenthesis removed
    
    Source: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
    """
    s = [*s]
    parenthesis_stack = []
    opening_tag, closing_tag = '(', ')'

    # The idea here is the append the index wherever we see the opening tag
    # instead of appending the tag itself like we did in valid_parenthesis
    for idx, char in enumerate(s):
        if char == opening_tag:
            parenthesis_stack.append(idx)
        elif char == closing_tag:
            if parenthesis_stack:
                parenthesis_stack.pop()
            else:
                s[idx] = ''

    # If by the end of the above loop we still have idxs with opening tags,
    # we can't close them, hence, they have to be removed
    for i in parenthesis_stack:
        s[i] = ''

    return ''.join(s)
