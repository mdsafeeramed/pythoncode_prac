import oracledb
import getpass

conn = oracledb.connect(user="hr", password="sr", dsn="localhost:1521/XEPDB1")
with conn.cursor() as cur:
   cur.execute("SELECT * from Departments")
   res = cur.fetchall()
   print(res)
   for x in res:
       print(x)


