class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = int(year)

    def start(self):
        return ("The Car is Starting ...")

    def car_info(self):
        return (f"Car: {self.year} {self.brand} {self.model}")

    def age(self,current_year):
        return current_year - self.year

car1 = Car("Toyota","LandCruiser","2015")
print(car1.start())
print(car1.car_info())
print(car1.age(2025))