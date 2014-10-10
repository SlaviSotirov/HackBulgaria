def nan_expand(n):
    res = ""
    end = "NaN"
    not_a = "Not a "
    for i in range(n):
        res += not_a
        if i == n-1:
            res += end

    return res


def main():
    print(nan_expand(0))
    print(nan_expand(2))
    print(nan_expand(4))


if __name__ == '__main__':
    main()
