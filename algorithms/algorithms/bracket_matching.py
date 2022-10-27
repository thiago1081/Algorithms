from stack import Stack

def has_matching_brackets(statement, brackets=(("[", "]"), ("{", "}"), ("(", ")"))):
    bStack = Stack()
    for char in statement:
        for startBracket, endBracket in brackets:
            if char == startBracket:
                bStack.push(startBracket)
            elif char == endBracket:
                topChar = bStack.pop()
                if topChar is None or topChar != startBracket:
                    return False
    return bStack.isEmpty()