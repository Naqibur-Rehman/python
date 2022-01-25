import sys

# def divide(a, b):
#     try:
#         print(a // b)
#     except ZeroDivisionError:
#         print("can't divide by zero")
#
#
# a1 = input("Enter first number : ")
# b1 = input("Enter second number : ")
# try:
#     a1 = int(a1)
#     b1 = int(b1)
#     divide(a1, b1)
# except ValueError:
#     print("Please input an integer value")


""" ---------------------- perfect program --------------------"""


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except EOFError:
            sys.exit(1)
        except:  # should be except ValueError
            print("Invalid number, try again")
        finally:
            print("The finally clause always executes")


first_number = getint("Please enter first number ")
second_number = getint("Please enter second number ")

try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("Can't divide by zero")
    sys.exit(2)
else:
    print("division performed successfully")
