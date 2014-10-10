def contains_digit(number, digit):
    string = str(number)
    char = str(digit)
    for symbol in string:
        if symbol == char:
            return True
    return False

print(contains_digit(143, 2))
