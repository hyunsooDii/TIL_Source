import sys
from myapp import Application, MenuItem
import MySQLdb
from addr_repository import AddressRepository
from addr_ui import *

import sqlite3 # 표준 모듈이라 따로 설치 x

class DBApp(Application):
    def __init__(self):
        super().__init__() # Applicatino class를 상속받겠다는 뜻
        # self.db = MySQLdb.connect(host="localhost", db='sqldb', user='root', passwd='1234', charset='utf8')
        self.db = sqlite3.connect("C:/temp/test.db")
        self.repo = AddressRepository(self.db)

    def create_menu(self,menu):
        menu.add(MenuItem("목록", self.print_list))
        menu.add(MenuItem("추가", self.add))
        menu.add(MenuItem("수정", self.update))
        menu.add(MenuItem("삭제", self.remove))
        menu.add(MenuItem("검색", self.search))
        menu.add(MenuItem("종료", self.exit))

    def print_list(self):
        try:

            total = self.repo.get_total()
            rows = self.repo.get_list()
            print_list(total, rows)

        except Exception as e:
            print(e)

    def add(self):
        data = input_addr_info()
        self.repo.insert(data)

        print("추가되었습니다.")
        self.db.commit()

    def update(self):
        try:
            name = input("이름 : ")
            data = self.repo.get_one(name)
            if not data:
                print(f"{name} 데이터가 없습니다.")
                return

            data = self.repo.input_new_addr(data)
            self.repo.update(data)

        except Exception as e:
            print(e)
    def search(self):
        try:
            name = input("검색할 이름 입력 : ")
            where = f"where name like '%{name}%'"
            total = self.repo.get_total(where)
            rows = self.repo.get_list(where)
            print_list(total, rows)

        except Exception as e:
            print(e)


    def remove(self):
        try:
            name = input("삭제할 정보의 이름 입력 : ")
            self.repo.remove(name)
            self.db.commit()
            print("삭제 완료")
        except Exception as e:
            print(e)

    def exit(self):
        answer = input("종료하시겠습니까?[y]/n ")
        if answer in ["y", "Y", ""]: # 대괄호는 생략할 수 있다. 아무 입력없이 Enter 치면 yes로 해석
            self.repo.close()
            self.db.close()
            sys.exit(0)

if __name__ == '__main__':
    app = DBApp()
    app.run()