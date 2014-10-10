def next_hack(n):
    while True:
        n += 1
        if is_hack(n):
            return n


def is_hack(n):
    n = bin(n)
    string = str(n)
    string = string[2:]
    if string == string[:: -1]:
        count = 0
        for s in string:
            if s == "1":
                count += 1
        if count % 2 == 1:
            return True
    return False


def main():
    print(next_hack(5))
    print(next_hack(8031))
    print(is_hack(8031))


if __name__ == '__main__':
    main()
