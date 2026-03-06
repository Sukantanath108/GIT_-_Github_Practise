class Vehicle:

    def __init__(self, vehicle, model, year):
        self.vehicle = vehicle
        self.model = model
        self.year = year
       # self.__name = name (private property/encapsulation)


    def type(self):

        print("Choose from one of these:")
        print("1. car")
        print("2. boat")
        print("3. plane")

        choose = input("Enter type: ").lower()

        if choose == "car":
            print("You chose car!")

        elif choose == "boat":
            print("You chose boat!")

        elif choose == "plane":
            print("You chose plane!")

        else:
            print("Invalid choice!")

        return choose


class Car(Vehicle):

    def __init__(self, vehicle, model, year):
        super().__init__(vehicle, model, year)

    def move(self):
        print("The car moves on roads")


class Boat(Vehicle):

    def __init__(self, vehicle, model, year):
        super().__init__(vehicle, model, year)

    def move(self):
        print("The boat sails in water")


class Plane(Vehicle):

    def __init__(self, vehicle, model, year):
        super().__init__(vehicle, model, year)

    def move(self):
        print("The plane flies in the sky")


car = Car("car","Toyota",2016)
boat = Boat("boat","Pinyata",2025)
plane = Plane("plane","Sparrow",2013)


vehicles = [car, boat, plane]

for v in vehicles:
    print(v.vehicle, v.model, v.year)
    v.move()


class PrivateProperty:
    def __init__(self,buy,sell):
        self.buy = buy
        self.__sell = sell #encapsulation

    def get_sell_value(self):
        return f"The private value of sell is -{self.__sell}"

    def set_sell_pv_value(self):
        if sell > 1000:
            self.__sell = sell
        else: # using set method to change private property value
            print("Madarchod")
    def __str__(self):
        return f"I bought it at{self.buy}$"
pv = PrivateProperty("50000",1222)

print(pv)
print(pv.get_sell_value())