def is_decreasing(seq):
    for i in range(len(seq)-1):
        if seq[i] <= seq[i+1]:
            return False
    return True


def main():
    print(is_decreasing([10, 8, 9, 4]))


if __name__ == '__main__':
    main()
