import MySQLdb

db = MySQLdb.connect(db="sqldb", host="localhost", user="root", passwd="1234",
charset='utf8')
cursor = db.cursor()
# cursor를 통해 SQL 문장 실행
# 자원 해제 및 접속 해제

cursor.execute('DROP TABLE IF EXISTS tblAddr')
cursor.execute("""
CREATE TABLE tblAddr(
 name CHAR(16) PRIMARY KEY,
 phone CHAR(16),
 addr TEXT
)
""")

cursor.execute("INSERT INTO tblAddr VALUES('김상형', '123-4567', '오산')")
cursor.execute("INSERT INTO tblAddr VALUES('한경은', '555-1004', '수원')")
cursor.execute("INSERT INTO tblAddr VALUES('한주완', '444-1092', '대전')")

db.commit()

table = cursor.fetchall()
for record in table:
 print(f"이름: {record[0]}, 전화: {record[1]}, 주소: {record[2]}")

cursor.close()
db.close()