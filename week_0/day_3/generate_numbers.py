import sys
from random import randint


def main():
    filename = sys.argv[1]
    randoms = int(sys.argv[2])
    file = open(filename, "w")
    for i in range(randoms):
        file.write(str(randint(1, 100)))
        file.write(" ")

    file.close()


if __name__ == '__main__':
    main()
