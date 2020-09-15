import MySQLdb

db = MySQLdb.connect(host="localhost", db='employees', user='root', passwd='1234')

cursor = db.cursor()

sql = """
"""
cursor.execute(sql)

rows = cursor.fetchall()
for row in rows:
    print(row)

# 필요한 작업 실행

cursor.close()
db.close()