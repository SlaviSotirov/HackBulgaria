def is_int_palindrome(n):
    temp1 = str(n)
    temp2 = temp1[::-1]
    return temp1 == temp2


print(is_int_palindrome(1011))
