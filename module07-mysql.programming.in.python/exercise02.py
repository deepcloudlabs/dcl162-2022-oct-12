from mysql import connector

mysql_connection = connector.connect(
    host="localhost",
    user="root",
    password="Secret_123",
    database="world"
)

my_cursor = mysql_connection.cursor()
my_cursor.execute("show tables")
for table_name in my_cursor:
    print(table_name[0])
