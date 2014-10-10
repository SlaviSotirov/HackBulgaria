from sum_divs import sum_of_divisors


def is_prime(n):
    if sum_of_divisors(n) == (n + 1):
        return True
    return False


#print (is_prime(100))
