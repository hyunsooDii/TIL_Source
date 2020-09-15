# 클래스 - 관련 정보와 정보의 조작 함수 (메소드)를 묶어서 관리

# balance = 8000
#
# def deposit(money):
#     global balance
#     balance += money
#
# def inquire():
#     print(f"잔액은 {balance}원 입니다.")
#
# deposit(1000)
# inquire()

# class 키워드로 정의 - 사용하기 위해서는 인스턴스를 생성한 후 사용, 클래스명은 대문자로 시작

# class Account:
#     def __init__(self, balance): # 앞뒤가 __인것은 파이썬 이용하는 함수, 작업할 인스턴스에 대한 참조
#         self.balance = balance
#
#     def doposit(self, money):
#         self.balance += money
#
#     def inquire(self):
#         print(f"잔액은{self.balance}원 입니다.")
#
# def main():
#     account = Account(8000)
#     account.doposit(1000)
#     account.inquire()
#
# main()

# 생성자 - __init__(self) - 인스턴스를 생성할 때 자동으로 호출, 멤버 변수 정의 및 초기화 역할

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def intro(self):
#         print(str(self.age)+"살 "+self.name+"입니다.")
#
#     def __str__(self): # 현재정보의 instance 를 문자열로 return 해주는 함수
#         return f"{self.age}살 {self.name} 입니다."
#
# def main():
#
#     name = input("이름 : ")
#     age = input("나이 : ")
#
#     kim = Human(name, age)
#     kim.intro()
#
#     print(kim.name)
#     kim.age = 20
#
#     name = input("이름 : ")
#     age = input("나이 : ")
#
#     lee = Human(name, age)
#     lee.intro()
#
# main()

# class Stack:
#     def __init__(self, size=5): # 매개변수에 값을 정해두면 그 값은 default 값
#         self.size = size
#         self.data = []
#
#     def push(self, data):
#         if len(self.data) == self.size: # Full
#             return
#         self.data.append(data)
#
#     def pop(self):
#         if len(self.data) == 0: # Empty
#             return
#         self.data.pop()
#
#     def clear(self):
#         self.data = []
#
#     def __str__(self): # __str__ 함수 - 인스턴스화 될 때
#         return f"Stack size : {self.size}, data {self.data}"
#
# def main():
#     stack = Stack()
#     stack.push(5)
#     stack.push(5)
#     stack.push(5)
#     stack.push(5)
#     stack.push(5)
#
#     print(stack)
#
#     print(stack.pop())
#
# main()

class UserInfo: # 순수하게 데이터만 갖고 있는 Class - Data Class
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"이름 : {self.name}, E-mail : {self.email}, 핸드폰 : {self.phone}"

    def __repr__(self):
        return f"이름 : {self.name}, E-mail : {self.email}, 핸드폰 : {self.phone}" # 컬렉션에 담겨져 있는 인스턴스 문자열 출력

# l = [
#     UserInfo("홍길동", "gsd@naver.com", "010-3434-3434"),
#     UserInfo("고길동", "fgdsk@naver.com", "010-3432-4333")
# ]
#
# u1 = UserInfo("홍길동", "gsd@naver.com", "010-3434-3434")
# u2 = UserInfo("고길동", "fgdsk@naver.com", "010-3432-4333")
# l = [u1, u2]
#
# print(l)
# print(l[0])
# print(l)

# def main():
#     print(UserInfo("홍길동", "gksd@gmail.com", "010-3434-3434"))
#
# main()

import pickle

class Addressbook:
    def __init__(self):
        self.book = []

    def add(self, name, email, phone):
        ui = UserInfo(name, email, phone)
        self.book.append(ui)

    def find_by_name(self, name):
        for ui in self.book:
            if ui.name == name:
                return ui

    def update(self, name, email, phone):
        ui = self.find_by_name(name)
        if not ui:
            print("목록에 없습니다.")
            return

        ui.email = email
        ui.phone = phone

    def remove(self, name):
        ui = self.find_by_name(name)
        if not ui:
            print(f"{name}은 목록에 없습니다")
            return

        self.book.remove(ui)

    # def search_by_name(self, name):
    #     new_book = []
    #     for ui in self.book:
    #         if ui.name.find(name) > -1:
    #             new_book.append(ui)
    #
    #     return new_book

    def search_by_name(self, name):
        return [ui for ui in self.book if ui.name.find(name) > -1]

    def save(self, fpath):
        try:
            with open(fpath, "wb") as file:
                pickle.dump(self.book, file)
        except Exception as e:
            print(f"{fpath} 파일 쓰기에 실패했습니다.")
            print(e)

    def load(self, fpath):
        try:
            with open(fpath, "rb") as file:
                self.book = pickle.load(file)
                return self.book
        except Exception as e:
            print(f"{fpath} 파일 읽기에 실패했습니다.")

    def sort(self):
        self.book.sort(key = lambda u: u.name)


    def __str__(self):
        pass

def main():
    # address = Addressbook()
    #
    # address.add("홍길동", "gdskgds@naver.com" ,"010-3243-5454")
    # address.add("고길동", "gdsdsaas@naver.com" ,"010-3993-5454")
    #
    # #print(address.book)
    #
    # address.update("고길동", "gds@naver.com", "010-3434-4361")
    # u1 = address.find_by_name("고길동")
    # #print(u1)
    # address.update("희동이", "gdsgds@naver.com", "010-3333-3333")
    #
    # u1 = address.search_by_name("길동")
    # #print(u1)
    #
    # address.remove("고길동")
    # u1 = address.find_by_name("고길동")
    # #print(u1)

    file_name = "book1.dat"
    addr_book = Addressbook()
    addr_book.load(file_name)

    addr_book.sort()
    print(addr_book.book)

    # addr_book.add("홍길동", "hong@naver.com", "010-1111-1111")
    # addr_book.add("고길동", "go@naver.com", "010-2222-2222")
    # addr_book.save(file_name, addr_book)

    # for ix in range(1, 100):
    #     if ix%2 == 0:
    #         addr_book.add(f"홍길동{ix}", "hong{ix}@naver.com", "010-1111-1111")
    #     else:
    #         addr_book.add(f"고길동{ix}", "go{ix}@naver.com", "010-2222-2222")
    #
    # addr_book.save(file_name)
    #
    # addr_book2 = Addressbook()
    # addr_book2.load(file_name)
    # print(addr_book2.book)

main()