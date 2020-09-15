import MySQLdb
db = MySQLdb.connect(host="localhost", db='employees', user='root', passwd='1234')

cursor = db.cursor()

print("접속에 성공했습니다.")

sql = """SELECT * FROM EMPLOYEES
ORDER BY hire_date DESC
LIMIT 10
"""
cursor.execute(sql)


rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
db.close()