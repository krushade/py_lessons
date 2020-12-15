class Car:

    MODELS = ('Toyota', 'Nissan', 'Honda',
              'Audi', 'Ford', 'Dodge', 'Volkswagen')
    COLORS = ('Blue', 'Red', 'White', 'Black', 'Green', 'Gray')

    def __init__(self, model: str, max_speed: int,
                 color: str, price: int):

        if model.title() in self.MODELS:
            self.__model = model.title()
        else:
            self.__model = None
            print("Invalid model.")

        if max_speed in range(1, 420):
            self.__max_speed = max_speed
        else:
            self.__max_speed = None
            print("Invalid max speed.")

        if color.title() in self.COLORS:
            self.__color = color
        else:
            self.__color = None
            print("Invalid color.")

        if 0 < price:
            self.__price = price
        else:
            self.__price = None
            print("Invalid price.")

    def __str__(self):
        data = {
            "Model": self.__model,
            "Max Speed": self.__max_speed,
            "Color": self.__color,
            "Price": self.__price
        }
        return f"Car data: {data}"

    def values(self):
        return {
            "Model": self.__model,
            "Max Speed": self.__max_speed,
            "Color": self.__color,
            "Price": self.__price
        }

    @property
    def model(self):
        return self.__model


if __name__ == '__main__':
    cars = []
    while True:
        enter_model = input(f"Please enter car model.\n"
                            f"Choose from {Car.MODELS}: ")
        enter_max_speed = int(input("Please enter max speed: "))
        enter_color = input(f"Please enter color.\n"
                            f"Choose from {Car.COLORS}: ")
        enter_price = int(input("Please enter price: "))

        car = Car(enter_model, enter_max_speed, enter_color, enter_price)
        print(car)
        cars.append(car)

        while True:
            again = input("Do you want to create another instance? (yes/no): ")
            if again in ('no', 'yes'):
                break
            else:
                print("Try again.")
                continue

        if again == 'no':
            for one_car in cars:
                car_value = []
                for v in one_car.values().values():
                    car_value.append(v)
                if None in car_value:
                    print(one_car)
                    print(car_value)
           # не могу удалить машину обращаясь к ее адресу

            for one_car in cars:
                print(one_car.__str__())
            break
