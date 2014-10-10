def count_consonants(s):
    count = len(s)
    for i in range(0, len(s)):
        if s[i] is "a" or s[i] is "e" or s[i] is "i":
            count -= 1
        elif s[i] is "o" or s[i] is "u" or s[i] is "y":
            count -= 1

    return count


def main():
    print(count_consonants("asdaseedasa"))

if __name__ == '__main__':
    main()
