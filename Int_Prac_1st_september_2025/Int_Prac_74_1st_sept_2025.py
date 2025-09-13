# 74) Connect to OracleDB server(Practice at PC)

import oracledb

conn = oracledb.connect(user="hr", password="gv", dsn="localhost:1521/XEPDB1")
with conn.cursor() as saf:
    saf.execute("SELECT * from Departments")
    res= saf.fetchall()
print(f"question 74 answer is : {res}")