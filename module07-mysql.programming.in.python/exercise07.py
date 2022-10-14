from mysql import connector

mysql_connection = connector.connect(
    host="localhost",
    user="root",
    password="Secret_123",
    database="banking"
)

my_cursor = mysql_connection.cursor()
my_cursor.execute("""
    set session transaction isolation level read uncommitted
    set session transaction isolation level read committed
    set session transaction isolation level repeatable read
    set session transaction isolation level serializable
""")

mysql_connection.commit()

"""
mysql> set session transaction isolation level read uncommitted;
Query OK, 0 rows affected (0.00 sec)

mysql> select @@transaction_isolation;
+-------------------------+
| @@transaction_isolation |
+-------------------------+
| READ-UNCOMMITTED        |
+-------------------------+
1 row in set (0.00 sec)
"""

print(f"{my_cursor.rowcount} row(s) deleted")

