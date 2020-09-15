from addr_models import Addr

class AddressRepository:
    def __init__(self, db):
        self.cursor = db.cursor()

    def close(self):
        self.cursor.close()

    def get_total(self, where=''):
        sql = "select count(*) from tblAddr " + where # 테이블명과 where 절 사이에 space 줘야함
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        return row[0]

    def get_list(self, where=''):
        sql = "select * from tblAddr " + where
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

    def insert(self, data):
        sql = "INSERT INTO tblAddr VALUES(%s, %s, %s)"
        self.cursor.execute(sql, (data.name, data.phone, data.addr))

    def remove(self, data):
        sql = "DELETE FROM tblAddr WHERE name = %s"
        self.cursor.execute(sql, (data))

    def update(self, name):
        pass

    def get_one(self, name):
        sql = "select * from tblAddr where name = %s"
        self.cursor.execute(sql, (name,))
        row = self.cursor.fetchone()
        rows = Addr(*row) # * 펼쳐서 mapping시키겠다
        return (Addr(*row) for row in rows) # 튜플이 아닌 address 모델 객체

    def input_new_addr(self, data):
        phone = input(f"전화번호({data[1]}): ")
        if not phone:
            phone = data[1]
        addr = input(f"주소({data[2]}): ")

        if not addr:
            addr = data[2]

        return data[0], phone, addr

    def update(self, data):
        sql = """
              UPDATE tblAddr SET 
                phone = %s,
                addr = %s
              WHERE name = %s"""

        self.cursor.execute(sql, (data.phone, data.addr, data.name))
        self.db.commit()
        print("수정 완료")
