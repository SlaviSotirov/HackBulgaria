def is_an_bn(word):
    count = 0
    for i in range((len(word) + 1)//2):
        if word[i] == "a":
            count += 1
        print(i)
    print(count)
    print(word.count("b"))
    return count == int(word.count("b"))


def main():
    print(is_an_bn(""))
    print(is_an_bn("rado"))
    print(is_an_bn("aaabb"))
    print(is_an_bn("aaabbb"))
    print(is_an_bn("bbbaaa"))
    print(is_an_bn("aaaaabbbbb"))


if __name__ == '__main__':
    main()
