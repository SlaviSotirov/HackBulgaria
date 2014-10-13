import sys


def main():
    result = 0
    filename = sys.argv[1]
    file = open(filename, "r")
    content = file.read()
    numbers = list(content.split(" "))
    numbers.remove('')
    for num in numbers:
        result += int(num)

    print(result)
    file.close()


if __name__ == '__main__':
    main()
