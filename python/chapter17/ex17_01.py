# 고급 문법 - 해당 객체의 __iter__() 메소드로 열거 가능 객체 흭득
#          - 매 루프마다 __next()__ 함수를 통해 다음 요소를 추출

# 모듈 - 열거 가능 객체

# nums = [11, 22, 33]
#
# it = iter(nums)
# while True:
#     try:
#         num = next(it)
#     except StopIteration:
#         break
#     print(num)

class Seq:
    def __init__(self, data):
        self.data = data
        self.index = -2

    def __iter__(self):
        self.index = -2 # 시작할 때 리스트번지 초기화
        return self

    def __next__(self):
        self.index += 2
        if self.index >= len(self.data):
            raise StopIteration

        return self.data[self.index:self.index+2]

def main():
    solarterm = Seq("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")

    for k in solarterm:
        print(k, end=',')

    print()

    for k in solarterm:
        print(k, end=',')

main()