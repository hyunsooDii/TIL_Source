import MySQLdb

db = MySQLdb.connect(host="localhost", db='sqldb', user='root', passwd='1234', charset='utf8')

cursor = db.cursor()

# cursor.execute('DROP TABLE IF EXISTS tblAddr')
# cursor.execute("""
# CREATE TABLE tblAddr(
#  name CHAR(16) PRIMARY KEY,
#  phone CHAR(16),
#  addr TEXT
# )
# """)
# name = input("이름을 입력하시오 : ")
# phone = input("전화번호를 입력하시오 : ")
# city = input("거주지를 입력하시오 : ")
#
# sql = "INSERT INTO tblAddr VALUES(%s, %s, %s)"
# cursor.execute(sql, (name, phone, city))

cursor.execute("INSERT INTO tblAddr VALUES('김상형', '123-4567', '오산')")
cursor.execute("INSERT INTO tblAddr VALUES('한경은', '555-1004', '수원')")
cursor.execute("INSERT INTO tblAddr VALUES('한주완', '444-1092', '대전')")


db.commit()

cursor.execute("""SELECT * FROM tblAddr
               ORDER BY addr""")
#
table = cursor.fetchall() # fetchall() 함수는 전부 출력
print(table)
for record in table:
 print(f"이름: {record[0]}, 전화: {record[1]}, 주소: {record[2]}")

# while True:
#  record = cursor.fetchone() # fetchone()함수는 한개 출력
#  if record == None: break
#
#  print(f"이름: {record[0]}, 전화: {record[1]}, 주소: {record[2]}")

# name = input("검색어(이름): ")

# cursor.execute(f"SELECT addr FROM tblAddr WHERE name ='{name}'")
# sql = "SELECT addr FROM tblAddr WHERE name = %s"
# cursor.execute(sql, (name,))

# record = cursor.fetchone() # fetchone에서 값이 없으면 none Return, fetchall에서 값이 없으면 비어있는 튜플 return

# if record : print(f"{name}은 {record[0]}에 살고 있습니다.")
# else: print(f"{name}은 없는 이름입니다.")

cursor.close()
db.close()