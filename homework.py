from uuid import uuid4

class Product:
    def __init__(self, name, price, quantity):
        self.__id = uuid4()
        self.name = name
        self.price = price
        self.quantity = quantity

    def info(self):
        return f"Mahsulot nomi: {self.name}, Narxi: {self.price}, Miqdori: {self.quantity}"

    def sell(self, amount):
        if amount > self.quantity:
            return f"Siz {amount}ta mahsulot so'radingiz, lekin omborda {self.quantity}ta bor."
        else:
            self.quantity -= amount
            return f"{amount}ta mahsulot sotildi. Omborda {self.quantity}ta qoldi."

    def restock(self, amount):
        self.quantity += amount
        return f"Omborga {amount}ta mahsulot qo'shildi. Yangi miqdor: {self.quantity}"

    def get_id(self):
        return f"Mahsulot ID:{self.__id}"

class Electronics(Product):
    def __init__(self, name, price, quantity, warranty):
        super().__init__(name, price, quantity)
        self.warranty = warranty

    def info(self):
        data = super().info()
        data += f", garantiya: {self.warranty}"
        return data


class Food(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date

    def info(self):
        data = super().info()
        data += f", Yaroqlilik muddati: {self.expiration_date}"
        return data

    def sell(self, amount):
        if self.expiration_date > "2025-02-11":
            return "Xatolik: mahsulot muddati o'tgan!"
        return super().sell(amount)

phone = Electronics("Iphone 15pro", "10.000.000"  , 30, "1year")
print(phone.info())
print(phone.sell(6))
print(phone.get_id())

hotdog = Food("Hot dog","15.000", 20, "1day")
print(hotdog.info())
print(hotdog.sell(5))
print(hotdog.get_id())


class Basket(Product):
    def __init__(self):
        self.__id = uuid4()
        self.products = []

    def add(self, product):
        self.products.append(product, self.price)
        return f"{product}  savatga qo'shildi"

    def show(self):
        print("Savat ichida:")
        for i in self.products:
            return f"- {i['product']}: {i['price']}"

    def calc(self):
        money = 0
        for i in self.products:
            money += i.price * i.quantity
        return money

    def remove(self, product_name):
        for i, (product, quantity) in enumerate(self.products):
            if product.name == product_name:
                product.restock(quantity)
                del self.products[i]
                return f"{product_name} savatdan olib tashlandi."


    def delete_basket(self):
        self.products.clear()
        return "Savat butunlay bo'shatildi!"


    def add2(self):
        self.products2 = self.products.copy()
        return f"Mahsulotlar 2chi savatga qo'shildi: {self.products2}"


 = Electronics("Laptop", 1200, 10, 2)
print()
print()
print()
print()



banana = Food("Banana",5000, 100, "3kun")
print(banana.info())
print(banana.sell(10))
print(banana.restock(20))
print(banana.get_id())
