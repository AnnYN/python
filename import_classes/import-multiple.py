#import多个class
from car import Car, ElectricCar
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_des_name())
my_tesla1 = ElectricCar('tesla','roadster',2016)
print(my_tesla1.get_des_name())