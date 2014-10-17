def prepare_meal(number):
    to_spam = False
    result = ""
    while True:
        if number % 3 == 0:
            if to_spam:
                result += " "
                to_spam = False
            result += "spam"
            number = number // 3
            to_spam = True
        else:
            break

    if number % 5 == 0:
        if to_spam:
            result += " and "
        result += "eggs"

    return result
