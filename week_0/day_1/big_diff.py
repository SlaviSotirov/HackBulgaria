def biggest_difference(arr):
    min = arr[0]
    max = arr[0]
    for a in arr:
        if a < min:
            min = a
        if a > max:
            max = a

    return min - max


def main():
    print(biggest_difference([1, 3, 5, 10, 132]))


if __name__ == '__main__':
    main()
