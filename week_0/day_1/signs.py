def what_is_my_sign(day, month):
    sign = (month * 100) + day
    if sign in range(121, 219):
        return "Aquarius"
    elif sign in range(220, 320):
        return "Pisces"
    elif sign in range(321, 420):
        return "Aries"
    elif sign in range(421, 521):
        return "Taurus"
    elif sign in range(522, 621):
        return "Gemini"
    elif sign in range(622, 722):
        return "Cancer"
    elif sign in range(723, 822):
        return "Leo"
    elif sign in range(823, 923):
        return "Virgo"
    elif sign in range(924, 1023):
        return "Libra"
    elif sign in range(1024, 1122):
        return "Scorpio"
    elif sign in range(1123, 1221):
        return "Sagittarius"
    else:
        return "Capricorn"


def main():
    print(what_is_my_sign(5, 8))
    print(what_is_my_sign(29, 1))
    print(what_is_my_sign(30, 6))
    print(what_is_my_sign(31, 5))
    print(what_is_my_sign(2, 2))
    print(what_is_my_sign(8, 5))
    print(what_is_my_sign(9, 1))


if __name__ == '__main__':
    main()
