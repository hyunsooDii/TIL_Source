# 상속 - 기존 클래스 정의를 그대로 자신의 것으로 취하는 방법

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def intro(self):
#         print(str(self.age) + "살 " + self.name + "입니다.")
#
# class Student(Human): # Student 클래스가 Human 클래스를 상속받음
#     def __init__(self, name, age, stunum):
#         super().__init__(name, age) # 일반적으로 상속받은 함수를 먼저 호출한 후 자신을 초기화
#         self.stunum = stunum
#
#     def intro(self):
#         super().intro() # 재정의 (method override)
#         print("학번 : " + str(self.stunum))
#
#     def study(self):
#         print("하늘천 따지 검을 현 누를 황")
#
# kim = Human("김상형", 29)
# kim.intro()
#
# lee = Student("이승우", 45, 930011)
# lee.intro()
# lee.study()

# 액세스 - 파이썬은 기본적으로 정보 은폐 기능 지원하지 않음, getter/setter로 정보(프로퍼티)를 보호

class Date:
    def __init__(self, month):
        self.inner_month = month

    @property
    def month(self):
        return self.inner_month

    @month.setter
    def month(self, month):
        if 1 <= month <= 12:
            self.inner_month = month
#
# def main():
#     today = Date(8)
#     today.month = 15
#
#     print(today.month)
#
# main()

# 프라이빗 멤버 변수 - 멤버 변수 앞에 __을 붙이면 외부에서 바로 접근 불가

# class Date:
#     def __init__(self, month):
#         self.__month = month
#
#     def setmonth(self, month):
#         if 1 <= month <=12:
#             self.__month = month
#
#     month = property(getmonth,setmonth())

# class Car:
#     @staticmethod
#     def hello():
#         print("오늘도 안전운행 합시다")
#
#     count = 0
#     def __init__(self, name):
#         self.name = name
#         Car.count += 1
#
#     @classmethod
#     def outcount(cls):
#         print(cls.count)
#
# def main():
#     Car.hello()
#
# main()

# 연선자 메소드

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other): # equal함수 오버라이드
        return self.name == other.name and self.age == other.age

def main():
    kim = Human("김상형", 22)
    sang = Human("김상형", 22)
    moon = Human("문종민", 44)

    print(kim == sang)
    print(kim == moon)

main()