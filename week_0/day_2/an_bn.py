def is_an_bn(word):
    count = 0
    for i in range((len(word) + 1)//2):
        if word[i] == "a":
            count += 1

    return count == int(word.count("b"))
