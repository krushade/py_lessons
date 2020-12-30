import sqlite3


def input_data():
    first = str(input("Enter your name: "))
    last = str(input("Enter your last name: "))
    age = int(input("Enter your age: "))
    city = str(input("Enter your city: "))
    return first, last, age, city


def input_in_db(first, last, age, city):
    connection = sqlite3.connect('log_data.db')
    c = connection.cursor()
    result = c.execute(
        "INSERT INTO info (first, last, age, city) VALUES (?, ?, ?, ?);",
        (first, last, age, city)
        )
    connection.commit()
    connection.close()
    return None


if __name__ == '__main__':
    while True:
        try:
            first, last, age, city = input_data()
        except Exception:
            print("Wrong data")
            answer = input("Try again? (y/n): ")
            if answer == 'n':
                break
            if answer == 'y':
                continue
        input_in_db(first, last, age, city)
        answer = input("Try again? (y/n): ")
        if answer == 'n':
            break
        if answer == 'y':
            continue
