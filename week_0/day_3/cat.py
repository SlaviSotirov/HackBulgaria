import sys


def main():
    for arg in sys.argv[1:]:
        filename = arg

        file = open(filename, "r")

        content = file.read()
        print(content)
        file.close()

if __name__ == '__main__':
    main()
