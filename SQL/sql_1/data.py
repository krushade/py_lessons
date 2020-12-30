import sqlite3

connection = sqlite3.connect('learn.db')
c = connection.cursor()
result = c.execute(
    """
    INSERT INTO user (name, data) VALUES ('vaZZgen', "12-22-2012");
    """
)
connection.commit()
connection.close()

if __name__ == '__main__':
