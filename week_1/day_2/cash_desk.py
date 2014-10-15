class CashDesk:
    def __init__(self):
        self.money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    def take_money(self, money):
        for m in money:
            self.money[m] += money[m]

    def total(self):
        total = 0
        for m in self.money:
            total += int(m) * self.money[m]
        print(total)

    def can_withdraw_money(self, money):
        temp_money = self.money
        not_changed = 0
        while True:
            for m in temp_money:
                if money > int(m) and temp_money[m] > 0:
                    temp_money[m] -= 1
                    money -= int(m)
                else:
                    not_changed += 1
            if money == 0:
                return True
            if not_changed > 100:
                return False


def main():
    my_cash_desk = CashDesk()
    my_cash_desk.take_money({1: 2, 50: 1, 20: 1})
    my_cash_desk.total()
    print(my_cash_desk.can_withdraw_money(30))
    print(my_cash_desk.can_withdraw_money(70))


if __name__ == '__main__':
    main()
