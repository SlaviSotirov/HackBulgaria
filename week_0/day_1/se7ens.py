
def sevents_in_a_row(arr, n):
    status = False
    for i in range(0, len(arr) - n):
        if arr[i] == 7:
            for a in range(i, i+n):
                if arr[a] != 7:
                    break
                if a == i+n-1:
                    status = True
            if status:
                break

    return status

print(sevents_in_a_row([1, 7, 2, 3, 4, 7, 7, 7, 7, 1], 4))
