class Car:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.quality = 100
        self.speed = 0

    def add_speed(self, additional_speed):
        self.speed += additional_speed

    def crash(self, other_car):
        self.quality = 0
        other_car.quality = 0


tesla = Car('Tesla', 'pink')
honda = Car('Honda', 'brown')

print(tesla.quality)
print(honda.quality)

tesla.crash(honda)

print(tesla.quality)
print(honda.quality)


class Garage:
    def __init__(self, max_size):
        self.max_size = max_size
        self.car_list = []

    def add_car(self, car):
        if len(self.car_list) < self.max_size:
            self.car_list.append(car)
        else:
            self.explode(self.car_list, car)

    def explode(self, cars, new_car):
        for car in cars:
            car.quality = 0
            print('BOOM!')
        new_car.quality = 0
        print('BOOM!')
        print('Yay!')
        self.car_list = []

home = Garage(2)

home.add_car(tesla)
home.add_car(honda)
duck = Car('Duck', 'green')
home.add_car(duck)
[print(i.brand) for i in home.car_list]