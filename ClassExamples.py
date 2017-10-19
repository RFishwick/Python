class Car:
    # Constructor Method _init_
    def __init__(self):
        print('Car created')
 
     # drive method
    def drive(self):
        print('Engine started')

class Hello:
    # Constructor Method _init_
    def __init__(self):
        print('Hello Method created')

    def say_hi(self):
        print('Hi!')
    
    def say_hello(self):
        print('Hello!')

    def say_hola(self):
        print('Hola!')
        
# create an object of type car, named superCar
superCar = Car()
 
# use drive method
superCar.drive()


greet = Hello()
greet.say_hi()
greet.say_hello()
greet.say_hola()
