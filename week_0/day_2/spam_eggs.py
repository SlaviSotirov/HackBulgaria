def prepare_meal(number):
    to_spam = False
    result = ""
    while True:
        if number % 3 == 0:
            result += "spam "
            number = number // 3
            to_spam = True
        else:
            break

    if number % 5 == 0:
        if to_spam:
            result += "and "
        result += "eggs"

    return result


def main():
    print(prepare_meal(9))
    print(prepare_meal(6))
    print(prepare_meal(27))
    print(prepare_meal(45))
    print(prepare_meal(1))


if __name__ == '__main__':
    main()
