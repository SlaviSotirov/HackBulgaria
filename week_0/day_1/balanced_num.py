def is_number_balanced(number):
    left = 0
    right = 0
    string = str(number)
    for x in range(0, (len(string)//2)):
        left += int(string[x])

    for x in range((len(string)//2), len(string)):
        right += int(string[x])

    return left == right


def main():
    print(is_number_balanced(221131))

if __name__ == '__main__':
    main()
