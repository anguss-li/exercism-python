def is_paired(input_string: str) -> bool:
    '''Check that all brackets in string are correctly paired.'''
    pairs = {'{': '}', '[': ']', '(': ')'}
    stack = []

    for char in input_string:
        if char in pairs:
            stack.append(char)
        elif char in pairs.values():
            # By removing reference bracket, pop allows function to match nested
            if not stack or char != pairs[stack.pop()]:
                return False

    return not stack