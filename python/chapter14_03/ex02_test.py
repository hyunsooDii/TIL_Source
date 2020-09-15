# import MySQLdb
#
# db = MySQLdb.connect(host="localhost", db='sqldb', user='root', passwd='1234', charset='utf8')
#
# cursor = db.cursor()
#
# cursor.execute('DROP TABLE IF EXISTS tblAddr')
# cursor.execute("""
# CREATE TABLE tblAddr(
#  name CHAR(16) PRIMARY KEY,
#  phone CHAR(16),
#  addr TEXT
# )
# """)
# try:
#     name = input("이름을 입력하시오 : ")
#     phone = input("전화번호를 입력하시오 : ")
#     city = input("거주지를 입력하시오 : ")
#
#     sql = "INSERT INTO tblAddr VALUES(%s, %s, %s)"
#
#     cursor.execute("INSERT INTO tblAddr VALUES('김상형', '123-4567', '오산')")
#     cursor.execute("INSERT INTO tblAddr VALUES('한경은', '555-1004', '수원')")
#     cursor.execute("INSERT INTO tblAddr VALUES('한주완', '444-1092', '대전')")
#     cursor.execute("UPDATE tblAddr SET addr = '제주도' WHERE name = '김상형'")
#     db.commit()
#
#     cursor.execute(sql, (name, phone, city))
#     print(cursor.fetchone())
#
#     # cursor.execute(f"INSERT INTO tblAddr VALUES('{name}','{phone}','{city}')")
#     db.commit()
# except Exception as e:
#     print(e)
#
# cursor.close()
# db.close()