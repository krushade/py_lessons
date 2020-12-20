class Car:

    def __init__(self, model: str, max_speed: int, color: str, price: int):
        self.model = model
        self.max_speed = max_speed
        self.color = color
        self.price = price

    def __str__(self):
        data = {
            "Model": self.model,
            "Max Speed": self.max_speed,
            "Color": self.color,
            "Price": self.price
        }
        return f"Car data: {data}"


if __name__ == '__main__':
    cars = []
    while True:

        while True:
            models = ('Toyota', 'Nissan', 'Honda',
                      'Audi', 'Ford', 'Dodge', 'Volkswagen')
            enter_model = input(f"Please enter car model.\n"
                                f"Choose from {models}: ")
            if enter_model.title() in models:
                enter_model = enter_model.title()
                break
            else:
                print("Invalid value, try again.")
                continue

        while True:
            enter_max_speed = input("Please enter max speed: ")
            if enter_max_speed.isdigit():
                if 0 < int(enter_max_speed) < 450:
                    enter_max_speed = int(enter_max_speed)
                    break
                else:
                    print("Invalid value, try again.")
                    continue
            else:
                print("Invalid value, try again.")
                continue

        while True:
            colors = ('Blue', 'Red', 'White', 'Black', 'Green', 'Gray',)
            enter_color = input(f"Please enter color.\n"
                                f"Choose from {colors}: ")
            if enter_color.title() in colors:
                enter_color = enter_color.title()
                break
            else:
                print("Invalid value, try again.")
                continue

        while True:
            enter_price = input("Please enter price: ")
            if enter_price.isdigit():
                if 0 < int(enter_price):
                    enter_price = int(enter_price)
                    break
                else:
                    print("Invalid value, try again.")
                    continue
            else:
                print("Invalid value, try again.")
                continue

        cars.append(Car(enter_model, enter_max_speed,
                        enter_color, enter_price))

        proceed = input("You want to create another instance? yes/no: ")
        if proceed.lower() == 'no':
            [print(x) for x in cars]
            break
