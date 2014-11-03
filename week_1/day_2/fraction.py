class Fraction:
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator
        self.simplify()

    def get_float(self):
        return self.nominator / self.denominator

    def simplify(self):
        for i in range(self.denominator, 0, -1):
            if self.nominator % i == 0 and self.denominator % i == 0:
                self.nominator = self.nominator // i
                self.denominator = self.denominator // i
                break

    def __eq__(self, other):
        return other.get_float() == self.get_float()

    def __lt__(self, other):
        return other.get_float() > self.get_float()

    def __gt__(self, other):
        return other.get_float() < self.get_float()

    def __add__(self, other):
        temp_nominator = self.nominator * other.denominator + other.nominator * self.denominator
        temp_denominator = other.denominator * self.denominator
        return Fraction(temp_nominator, temp_denominator)

    def __sub__(self, other):
        temp_nominator = self.nominator * other.denominator - other.nominator * self.denominator
        temp_denominator = other.denominator * self.denominator
        return Fraction(temp_nominator, temp_denominator)


def main():
    a = Fraction(1, 2)
    b = Fraction(1, 2)
    c = Fraction(3, 10)

    print(a == b)
    print(a < c)
    print(a > c)


if __name__ == '__main__':
    main()
