def contains_digits(number, digits):
    string = str(number)
    status = False
    for n in digits:
        status = False
        for c in string:
            if str(n) == c:
                status = True
        if not status:
            return False
    return True

print(contains_digits(12341, [5, 2, 4]))
