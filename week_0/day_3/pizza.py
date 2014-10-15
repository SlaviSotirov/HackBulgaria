import sys
from time import time
from datetime import datetime

MENU = """Uknown command!
Try one of the following:
take <name> <price>
status
save
list
load <number>
finish"""


def get_input():
    command = input("Enter command>")
    return(command)


def take_order(command):
    command = command.split(" ")
    name = command[1]
    price = int(command[2])
    print("Taking order from {} for {}".format(name, price))

    return [name, price]


def update_status(status, order):
    if order[0] in status:
        status[order[0]] += order[1]
    else:
        status[order[0]] = order[1]

    return status


def print_status(status):
    for item in status:
        print("{} - {}". format(item, status[item]))


def save_file(status):
    ts = time()
    stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    filename = "order_" + stamp
    order_file = open(filename, "w")
    for item in status:
        order_file.write(item + " - " + str(status[item]) + "\n")
    order_file.close()
    print("Saved the current order to " + filename)


def main():

    option = ""
    order = []
    status = {}
    to_exit = False
    while not to_exit:
        option = get_input()

        if option.split(" ")[0] == "take":
            order = take_order(option)
            status = update_status(status, order)
        elif option.split(" ")[0] == "finish":
            to_exit = True
        elif option.split(" ")[0] == "status":
            print_status(status)
        elif option.split(" ")[0] == "list":
            pass
        elif option.split(" ")[0] == "save":
            save_file(status)
        elif option.split(" ")[0] == "load":
            pass
        else:
            print(MENU)


if __name__ == '__main__':
    main()
