# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# i = int(input("enter a number"))
# #output  nr is greater than 5, number is = to 5, else say smaller than 5
# if i > 5:
#     print("the number is greater than 5")
# elif i == 5:
#     print("the number is equal to 5")
# else:
#     print("the nr is smaller than 5")

# def summation (start, end):
#     value = 0
#     for i in range (start, end+1, 1):
#         value = value + i
#     return value
# def summation2(a, b):
#     return b*(b+1)/2 - (a-1)*a/2
#
# n1 = 10
# n2 = 20
# result = summation(n1, n2)
# print (" the sum of " + str(n1) + " to " + str(n2) + " is " + str(result))
# print (" the sum of " + str(n1) + " to " + str(n2) + " is " + str(summation2(n1, n2)))
#
# def summation3(a, b):
#     area = b * a
#     return area
#
# a = 10
# b = 20
# print (" the area of rectangle is " + str(result))
#
# def summation4(a, *b):
#     return a+ sum (b)
#
# print(summation4(1,2))
# print(summation4(1,2,3))
# print(summation4(1,2,3,4))
#
# def method(a, id):
#     a[id] = -1
#
# field = [1,2,3,4,5]
# print(field)
# method(field, 0)
# print(field)
# method(field, 3)
# print(field)

#radius r to a function, calculate
# import math
#
# def circumfrance(r):
#     c = 2*math.pi*r
#     return c
# r = int(input())
# result = circumfrance(r)
# print(" Circumfrance of this cicrle for radius " ,r "is" ,result)

class Address:
    def __init__(self, street, number, postalcode, city):
        self.street = street
        self.number = number
        self.postalcode = postalcode
        self.city = city
    def getAddress(self):
        return self.street + "" + str(self.number) + ", " +\
            str(self.postalcode) + ", " + self.city

    def get_street(self):
        return self.street

    def get_postalcode(self):
        return self.postalcode

    def get_street(self):
        return self.street

    def get_postalcode(self):
        return self.postalcode

