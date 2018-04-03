#import某个class
from  car import ElectricCar
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_des_name())
my_tesla.battery.des_battery()
my_tesla.battery.get_range()

