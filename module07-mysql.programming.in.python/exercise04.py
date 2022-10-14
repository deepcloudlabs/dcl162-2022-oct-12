from mysql import connector

mysql_connection = connector.connect(
    host="localhost",
    user="root",
    password="Secret_123",
    database="banking"
)

my_cursor = mysql_connection.cursor()
my_cursor.execute("""
    select iban, balance
    from accounts
    limit 0,10
""")

for row in my_cursor:
    print(f"iban: {row[0]}\tbalance: {row[1]}")
