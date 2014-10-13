import sys


def count_chars(string):
    return len(string)


def count_words(string):
    a = ["?", ":", "!", ",", "\n", " ", "-"]
    new_string = ""

    for i in string:
        if i not in a:
            continue
        else:
            new_string += " "

    return(len(new_string.split(" ")))


def count_lines(string):
    return(len(string.splitlines()))


def main():
    wc_filfename = sys.argv[1]
    option = sys.argv[2]

    wc_file = open(wc_filfename, "r")
    content = wc_file.read()

    if option == "lines":
        print(count_lines(content))
    elif option == "chars":
        print(count_chars(content))
    elif option == "words":
        print(count_words(content))

    wc_file.close()

if __name__ == '__main__':
    main()
