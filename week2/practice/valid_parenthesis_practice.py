def is_valid_parentheses(s):
    stack = []
    mapping = { ')': '(', '}': '{', ']': '[' }

    for char in s:
        if char in mapping:
            if stack:
                top_element = stack.pop()
            else:
                top_element = '#'

            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack


print(is_valid_parentheses("()[]{}"))   # Output: True
print(is_valid_parentheses("([)]"))     # Output: False
