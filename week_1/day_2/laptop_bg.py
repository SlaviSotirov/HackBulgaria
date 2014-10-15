class Product:

    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        return self.final_price - self.stock_price


class Laptop(Product):
    def __init__(self, name, stock_price, final_price, diskspace, ram):
        super().__init__(name, stock_price, final_price)
        self.diskspace = diskspace
        self.ram = ram


class Smartphone(Product):
    def __init__(self, name, stock_price, final_price, display_size, mega_pixels):
        super().__init__(name, stock_price, final_price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels


class Store:
    def __init__(self, name):
        self.name = name
        self.products = {}
        self._total_income = 0

    def load_new_products(self, product, count):
        if product.name in self.products:
            self.products[product.name] += count
        else:
            self.products[product.name] = count

    def list_products(self):
        for p in self.products:
            print("{} - {}".format(p, self.products[p]))

    def sell_product(self, product):
        if product.name in self.products and self.products[product.name] > 0:
            self.products[product.name] -= 1
            self._total_income += int(product.profit())
            return True
        else:
            return False

    def total_income(self):
        print(self._total_income)


def main():
    new_product = Product("Kon", 100, 200)
    new_product.profit()
    new_laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)
    new_laptop.profit()
    new_smartphone = Smartphone('Hack Phone', 500, 820, 7, 10)
    new_smartphone.profit()
    store = Store("The magazin")
    store.load_new_products(new_smartphone, 2)
    store.load_new_products(new_laptop, 10)
    print(store.sell_product(new_smartphone))
    print(store.sell_product(new_smartphone))
    print(store.sell_product(new_smartphone))

    store.list_products()
    store.total_income()

if __name__ == '__main__':
    main()
