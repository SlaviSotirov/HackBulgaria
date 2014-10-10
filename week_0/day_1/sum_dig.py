def sum_of_digits(n):
    sum = 0
    n = abs(n)
    while n:
        sum += int(n) % 10
        n = int(n) / 10

    return sum


def main():
    print (sum_of_digits(12))


if __name__ == '__main__':
    main()
