import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False
def check_brackets():
    text = sys.stdin.read()
    opening_brackets_stack = []
    indexes = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(next)
            indexes.append(i)
        elif next == ')' or next == ']' or next == '}':
            if not opening_brackets_stack:
                return i+1
            else:
                top = opening_brackets_stack.pop()
                index = indexes.pop()
                if not Bracket(top, i).Match(next):
                    return i+1

    if not opening_brackets_stack:
        return True
    else:
        if indexes:
            return indexes[0]+1
        else:
            return i+1



if __name__ == "__main__":
    result = check_brackets()
    if result:
        print("Success")
    else:
        print(result if result > 0 else 1)
    
