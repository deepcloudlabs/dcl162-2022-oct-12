from mysql import connector

mysql_connection = connector.connect(
    host="localhost",
    user="root",
    password="Secret_123",
    database="banking"
)

my_cursor = mysql_connection.cursor()
my_cursor.execute("""
    update accounts
    set balance = balance - 28.50
""")

mysql_connection.commit()

print(f"{my_cursor.rowcount} row(s) updated")

