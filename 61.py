#Статические методы
class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def display(self):
        return f"{self.month}-{self.day}-{self.year}"

    @classmethod
    def millenium_c(cls, month, day):
        return cls(month, day, 2000)

    @staticmethod
    def millenium_s(month, day):
        return Date(month, day, 2000)
    