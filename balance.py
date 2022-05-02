from Stack import Stack


def check_balance(some_string: str = '') -> bool:
    string_to_check = some_string
    left_symbols = ['(', '[', '{']
    right_symbols = [')', ']', '}']
    supporting_stack = Stack()

    if len(string_to_check) == 0:
        return True

    for symbol in string_to_check:
        if symbol not in left_symbols + right_symbols:
            return False
        if symbol in left_symbols:
            supporting_stack.push(symbol)
        else:
            symbol_from_stack = supporting_stack.pop()
            if symbol_from_stack is None:
                return False
            if left_symbols.index(symbol_from_stack) != right_symbols.index(symbol):
                return False
    if supporting_stack.size() == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(check_balance('[{}]'))



