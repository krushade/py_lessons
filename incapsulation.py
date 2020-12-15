class Person:

    def __init__(self, name):
        self.__name = name
        self.__age = 1

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 120):
            self.__age = age
        else:
            print("Age incorrect")

    @property
    def name(self):
        return self.__name

    # def set_age(self, age):
    #     if age in range(1, 120):
    #         self.__age = age
    #     else:
    #         print("Age incorrect")

    def display_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")


if __name__ == '__main__':
    tom = Person("Tom")
    tom.display_info()