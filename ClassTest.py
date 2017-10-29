# Job to test Python classes

#Define variable values
color = "blue"

class Car:
    # info = []
    info = "black"
    
    # Constructor Method _init_
    def __init__(self):
        print('Car created')

     # drive method
    def drive(self):
        print('Engine started')
        
    # paint method
    def paint(self, hue):
        self.info.append(hue)
        
    def show(self):
        print(self.info)
 
class ShoppingList:
    products = []
 
    def __init__(self):
        print('Shopping list created')
 
    def add(self, name):
        self.products.append(name)
 
    def show(self):
        print(self.products)


# Begin Main
print("Begining ClassTest Program\n")
print("The color is {}.\n".format(color))

print("_"*20)
print("Car Info")
# create an object of type car, named superCar
superCar = Car()
superCar.paint(color)
superCar.show()

# use drive method
superCar.drive()

print("_"*20)
print("Go Shopping")
groceries = ShoppingList()
groceries.add('Peanutbutter')
groceries.add('Milk')
groceries.add('Life Cereal')
groceries.add(color)
groceries.show()
