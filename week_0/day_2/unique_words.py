from count_words import count_words


def unique_words_count(arr):
    return len(count_words(arr))


def main():
    print(unique_words_count(["apple", "banana", "apple", "pie"]))
    print(unique_words_count(["python", "python", "python", "ruby"]))


if __name__ == '__main__':
    main()
