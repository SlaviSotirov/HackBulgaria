#1,2,100,5,10,50,20
def calculate_coins(f):
    coins = {
        "1": 0,
        "2": 0,
        "100": 0,
        "5": 0,
        "10": 0,
        "50": 0,
        "20": 0
    }
    f = int(f * 100)
    while f:
        if f - 100 >= 0:
            f -= 100
            coins["100"] += 1
        elif f - 50 >= 0:
            f -= 50
            coins["50"] += 1
        elif f - 20 >= 0:
            f -= 20
            coins["20"] += 1
        elif f - 10 >= 0:
            f -= 10
            coins["10"] += 1
        elif f - 5 >= 0:
            f -= 5
            coins["5"] += 1
        elif f - 2 >= 0:
            f -= 2
            coins["2"] += 1
        elif f - 1 >= 0:
            f -= 1
            coins["1"] += 1
        else:
            break

    return coins


def main():
    print(calculate_coins(0.53))
    print(calculate_coins(1))


if __name__ == '__main__':
    main()
