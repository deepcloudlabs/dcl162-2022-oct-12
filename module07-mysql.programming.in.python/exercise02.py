from mysql import connector

mysql_connection = connector.connect(
    host="localhost",
    user="root",
    password="Secret_123",
    database="banking"
)

my_cursor = mysql_connection.cursor()
my_cursor.execute("""
    create table accounts(
        iban varchar(48) primary key,
        balance float default 10.0,
        status enum('ACTIVE', 'CLOSED', 'BLOCKED') default 'ACTIVE'
    ) engine=innodb
""")

"""
mysql> use banking
Database changed
mysql> show tables;
+-------------------+
| Tables_in_banking |
+-------------------+
| accounts          |
+-------------------+
1 row in set (0.00 sec)

mysql> desc accounts;
+---------+-----------------------------------+------+-----+---------+-------+
| Field   | Type                              | Null | Key | Default | Extra |
+---------+-----------------------------------+------+-----+---------+-------+
| iban    | varchar(48)                       | NO   | PRI | NULL    |       |
| balance | float                             | YES  |     | 10      |       |
| status  | enum('ACTIVE','CLOSED','BLOCKED') | YES  |     | ACTIVE  |       |
+---------+-----------------------------------+------+-----+---------+-------+
3 rows in set (0.00 sec)
"""