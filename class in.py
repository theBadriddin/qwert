# class Basket:
#     def __init__(self):
#         self.data = []
#
#     def add(self, product, price):
#         self.data.append({'product': product, 'price': price})
#         print(f"{product} ({price}) savatga qo'shildi")
#
#     def remove(self, product):
#         for item in self.data:
#             if item['product'] == product:
#                 self.data.remove(item)
#                 print(f"{product} savatdan olib tashlandi")
#                 return
#         print(f"{product} savatda topilmadi")
#
#     def show(self):
#         if not self.data:
#             print("Savat bo'sh")
#         else:
#             print("Savat tarkibi")
#             for item in self.data:
#                 print(f"- {item['product']}: {item['price']}")
#
#     def calculating(self):
#         total = sum(item['price'] for item in self.data)
#         print(f"Umumiy narx: {total}")
#
#
# basket = Basket()
# basket.add("qulpinay", 2)
# basket.add("Banan", 1)
# basket.show()
# basket.calculating()
# basket.remove("qulpinay")
# basket.show()+


#############################################################################################


# w = "absabsabsabsassssbs"
# k = "abs"
#
# count = w.count(k)
#
# while count > 0:
#     print(k * count)
#     count -= 1
################################################################
# from uuid import uuid4
#
# class Avto:
#     def __init__(self,name , year ):
#         self.__id = uuid4()
#         self.name = name
#         self.year = year
#         self.__km = 0
#
#     def get_km(self):
#         return f"Probeg:{self.__km}"
#
#     def get_id(self):
#         return f"Avtomobil ID:{self.__id} "
#
#
# a = Avto("Gentra", 2024)
# a.__km = 1000
# a.familiya = "Baxtiyorov"
#
# print(a.name , a.year)
# print(a.get_km())
# print(a.familiya)
# print(a.get_id())

#################################################################


# class Math:
#     def add(self , a , b):
#         return a + b
#
#     def add(self , a , b , c):
#         return a + b + c
#
#
# m = Math()
# print(m.add( 2 , 3 , 5))


##################################################################

#
# from abc import  ABC , abstractmethod
#
#
# class Person(ABC):
#     @abstractmethod
#     def speak(self):
#         pass
#
#
# class English(Person):
#     def speak(self):
#         print("I can speak")
#
#
# e = English()
# e.speak()

#####################################################################

from abc import ABC