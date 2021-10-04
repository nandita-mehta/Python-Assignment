import mysql.connector


def my_generator(cursor, array_size=1000):
    while True:
        results = cursor.fetchmany(array_size)
        if not results:
            break
        for x in results:
            yield x


my_db = mysql.connector.connect(host='localhost', user='root', password='password', port='3306', database=input("Enter database name:"))
my_cursor = my_db.cursor()
table_name = input("Enter table name:")
my_cursor.execute("select * from ", {table_name})
for x in my_generator(my_cursor):
    print(x)