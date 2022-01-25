""" Class: template for creating object. All objects created using same class will have same characteristics.
 Object: an instance of a class.
 Instantiate: create an instance of class.
 Method: a function defined in class.
Attributes: a variable bound to an instance of a class.
"""


class Kettle(object):

    power_source = "ELECTRICITY"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 9)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12
print(kenwood.price)

hamilton = Kettle("Hamilton", 15)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_on()

print("*" * 60)

kenwood.power = 1.5
print(kenwood.power)
# print(hamilton.power)

print("Switch to atomic power")
Kettle.power_source = "Atomic"
print(Kettle.power_source)
print("switch kenwood to gas")
kenwood.power_source = "gas"
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
