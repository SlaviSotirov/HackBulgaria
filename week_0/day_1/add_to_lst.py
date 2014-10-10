def number_to_list(n):
    string = str(n)
    li = []
    for s in string:
        li.append(int(s))

    return li


def main():
    print(number_to_list(12034))


if __name__ == '__main__':
    main()
