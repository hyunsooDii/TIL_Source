# 컬렉션

# 리스트의 사본 - 시퀀스.copy -> 시퀀스 복사본
# 숫자, bool은 stack에 저장되고, 시퀀스는 Heap영역에 저장됨 (주소값을 참조함)

import copy

# def main():
#     list1 = [1, 2, 3]
#     list2 = list1.copy() # list2 = list[:]
#
#     print(list1 == list2)
#
# main()

# def main():
#     list0 = ['a', 'b']
#     list1 = [list0, 1, 2]
#     list2 = list1.copy() # 얕은 복사, list1을 그대로 복사하여 복사본 생성
#     list3 = copy.deepcopy(list1) # 깊은 복사, 모든 참조된 값을 추적하여 복사본을 생성
#
#     list2[0][1] = 'c'
#     print("list0의 값 : ", list0)
#     print("list1의 값 : ", list1)
#     print("list1을 얕은 복사한 list : ", list2)
#     print("list1을 깊은 복사한 list : ", list3)
#
# main()

def test(numbers):
    numbers[0] = -1
    print(numbers)

def main():
    list1 = [1, 2, 3]
    test(list1) # 참조되는 list의 0번째 index 값을 -1로 바꾸는 함수 - call by reference
    print(list1)

main()