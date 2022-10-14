from mysql import connector

mysql_connection = connector.connect(
    host="localhost",
    user="root",
    password="Secret_123",
    database="banking"
)

my_cursor = mysql_connection.cursor()
my_cursor.execute("""
    insert into accounts values 
    ("TR1", 100000.0, 'ACTIVE'),
    ("TR2", 200000.0, 'CLOSED'),
    ("TR3", 300000.0, 'ACTIVE'),
    ("TR4", 400000.0, 'BLOCKED'),
    ("TR5", 500000.0, 'ACTIVE')
""")

mysql_connection.commit()
print(f"{my_cursor.rowcount} row(s) inserted")

"""
mysql> use banking
Database changed
mysql> select * from accounts;
+------+---------+---------+
| iban | balance | status  |
+------+---------+---------+
| TR1  |  100000 | ACTIVE  |
| TR2  |  200000 | CLOSED  |
| TR3  |  300000 | ACTIVE  |
| TR4  |  400000 | BLOCKED |
| TR5  |  500000 | ACTIVE  |
+------+---------+---------+
5 rows in set (0.00 sec)
"""