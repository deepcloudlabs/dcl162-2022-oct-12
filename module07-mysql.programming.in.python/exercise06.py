from mysql import connector

mysql_connection = connector.connect(
    host="localhost",
    user="root",
    password="Secret_123",
    database="banking"
)

my_cursor = mysql_connection.cursor()
my_cursor.execute("""
    delete from accounts
    where status='CLOSED'
""")

mysql_connection.commit()

print(f"{my_cursor.rowcount} row(s) deleted")

