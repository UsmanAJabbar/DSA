def balanced_parenthesis(s: str) -> str:
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

print(
    balanced_parenthesis(
        "(a(b(c)d)"
    )
)
