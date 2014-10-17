from fractions import gcd


def simplify_fraction(fraction):
    nominator = fraction[0]//gcd(fraction[0], fraction[1])
    denominator = fraction[1]//gcd(fraction[0], fraction[1])
    return (nominator, denominator)
