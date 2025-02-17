# class animal:
#     def sound(self):
#         print("Qandaydur hayvon ovozi")
#
# class dog(animal):
#     def sound(self):
#         print("woooof , woof")
#
# class cat(animal):
#     def sound(self):
#         print("Miov, miov")
#
# class goat(animal):
#     def sound(self):
#         print("Meee , meee")
#
# dog = dog()
# cat = cat()
# goat = goat()
#
# print(dog.sound())
# print(cat.sound())
# print(goat.sound())
#############################################################################################
#
#
#
#
#
# class flyable:
#     def fly(self):
#         print("ucha olaman")
#
# class walkable:
#     def walk(self):
#         print("yura olaman")
#
#
# class bird(flyable , walkable):
#     pass
#
#
# bird = bird()
# print(bird.fly())
# print(bird.walk())
# #############################################################################################
#
# class Transport:
#     def move(self):
#         return "Men ... harakatlanaman"
#
#
# class Car(Transport):
#     def move(self):
#         return "Men yo'lda yuraman"
#
# class Helicopter(Transport):
#     def move(self):
#         return "Men osmonda uchaman"
#
# class Train(Transport):
#     def move(self):
#         return "Men temir yo'lda yuraman"
#
# Car = Car()
# Helicopter = Helicopter()
# Train = Train()
#
# print(Car.move())
# print(Helicopter.move())
# print(Train.move())
#########################################################################################
#
# class Person:
#     def __init__(self , name , sourname, age):
#         self.name = name
#         self.sourname = sourname
#         self.age = age
#
#     def say_hi(self):
#         print("Salom")
#
# class Student(Person):
#     def say_hi(self):
#         print("Assalomu aleykum")
#
# class Pupil(Person):
#     pass
#
#
# s = Student("Badriddin", "Baxtiyorov", 17)
# p = Pupil("Badriddin", "Baxtiyorov" , 17)
##########################################################################
from itertools import cycle


# lst = [1, 2, 3, 4, 5, 6, 7, 8, 69, -2]
# largest = 0
#
# for i in range(len(lst)):
#     if lst[i] > lst[i - 1]:
#         largest = lst[i]
# print(largest)
####################################################################################


####################################################################################
# class Transport:
#     def __init__(self , name , speed):
#         self.name = name
#         self.speed = speed
#     def info(self):
#         print(f"Mening modelim {self.name} va tezligim {self.speed} ")
#
# class Car(Transport):
#     def info(self):
#         print(f"Avtomobilning modeli:{self.name} va uning tezligi:{self.speed}")
#
#
# class Bicycle(Transport):
#     def info(self):
#         print(f"Velosipedning modeli:{self.name} va uning tezligi:{self.speed}")
#
#
#
# c = Car("Gentra" , 220)
# v = Bicycle("Skillmax",  50)
# c.info()
# v.info()
#####################################################################################

class Product:
    def __init__(self , name , price , quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def info(self):
        return f"{self.name} - {self.price} x {self.quantity}"

    def sell(self, amount):
        if amount > self.quantity:
            print(f"Bizda {self.quantity} ta mahsulot bor xolos")
        else:
            self.quantity -= amount

    def restock(self, amount):
        self.quantity += amount

class Electronics(Product):
    def warranty(self , warranty):
        self.warranty = warranty
        print(f"{self.name}ga 1yil kafolat beriladi")


class Food(Product):
    def expiration_date(self):
        print()

lst = [12 , 13 , 14 , 15 , 18 , 20]
def num_plus():
    print()
