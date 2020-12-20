class Person:

    def __init__(self, gender, name, age):
        self.gender = gender
        if gender not in ('мужчина', 'женщина'):
            raise ValueError("GenderError")
        self.name = name
        self.age = age
        if 0 > age > 120:
            raise ValueError("AgeError")

    def gender_print(self):
        print(f"{self.name} {self.gender} и хрен поспоришь.")

    def age_print(self):
        if self.age < 18:
            print(f"{self.name}, возраст: {self.age}... мелочь")
        elif 17 < self.age < 50:
            print(f"{self.name}, возраст: {self.age}... средний возраст")
        elif 49 < self.age:
            print(f"{self.name}, возраст: {self.age}... пожилой")

    def info_print(self):
        print(f"Имя: {self.name}\n"
              f"Возраст: {self.age}\n"
              f"Пол: {self.gender}")


adam = Person('мужчина', 'Адам', 19)

eva = Person('женщина', 'Ева', 17)

if __name__ == '__main__':
    adam.age_print()
    adam.gender_print()
    adam.info_print()
    print('\n')
    eva.age_print()
    eva.gender_print()
    eva.info_print()