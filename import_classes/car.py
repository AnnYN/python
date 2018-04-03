class Car():
    def __init__(self, make, model, year):  # 初始化
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_des_name(self):  # 读取汽车信息
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def update_odometer(self, mileage):  # 更新里程数
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer")

    def increment_odometer(self, miles):  # 增加里程数
        self.odometer_reading += miles

    def read_odometer(self) :  # 读取里程数
        print("This car has " + str(self.odometer_reading) + " miles on it")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


# instance as attributes
class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def des_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += "miles on a full charge"
        print(message)



