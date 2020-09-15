# 리스트

# def main():
#     #nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ]
#     nums = list(range(10)) # 위에랑 같은거
#     print(nums[:])
#     print(nums[2:5])
#     print(nums[:4])
#     print(nums[6:])
#     print(nums[1:7:2])
#
#     score = [88, 95, 70, 100, 99]
#     print(score[2])
#     score[2] = 55
#     print(score[2])
#
#     nums2 = nums
#     print(nums == nums2)
#     nums2[0] = -1
#     # 리스트의 메모리관리는 Stack 영역이 아닌 Heap 영역에서 관리, 즉 17번째 줄에서 대입을 하였을 때 두 변수는 같은 주소값을 가지게 됨
#     # 데이터 복사가 아닌 데이터 주소(참조-reference 값) 복사
#     print(nums)
#     print(nums2)
#     print(nums == nums2)
#
#     print(id(nums)) # 두 변수의 같은 데이터 주소 확인가능
#     print(id(nums2))
#
#     nums = list(range(10))
#     nums2 = list(range(10))
#     print(nums == nums2)
#
#     # 숫자, Boolean 을 제외한 나머진 전부 데이터 주소 복사
#
#     nums2 = nums[:] # 슬라이싱에 의해 새로만들어진 데이터에 대해서 참조하겠다 라는 뜻, 즉 heap 영역에서 값을 갖고 새로운 heap 영역을 만들어 그 참조 값을 받아옴
#
# main()

# def main():
#     nums = list(range(10))
#     nums[2:5] = [20, 40] # 삽입하려는 갯수가 더 적으면 리스트 갯수를 삭제시켜버림
#     print(nums)
#     nums[6:8] = [60, 70, 80, 90] # 삽입하려는 갯수가 더 많으면 먼저 전에 있던 데이터를 삭제한 후, 갯수만큼 늘려서 삽입
#     print(nums)
#     nums[6:6] = [100, 200] # 기존의 리스트 값을 삭제하지 않고 추가하고 싶을 경우
#     print(nums)
#
# main()

# def main():
#     list1 = list(range(1,6))
#     list2 = [10, 11]
#     listadd = list1 + list2
#     print(listadd)
#     listmulti = list2 * 3
#     print(listmulti)
#
# main()

# def main():
#     lol = [
#         [1, 2, 3],
#         [4, 5],
#         [6, 7, 8, 9]
#     ]
#
#     print(lol[0])
#     print(lol[2][1])
#
#     for sub in lol:
#         for item in sub:
#             print(item, end=',')
#         print()
#
# main()

# def get_student_score(student):
#         subject_total = 0
#         for subject in student:
#             subject_total += subject
#
#         return subject_total
#
# def serve_subject(subject_total, student):
#     subjects = len(student)  # 과목의 수
#     avg = subject_total / subjects
#
#     return subjects
#
# def print_subject(subject_total, student):
#     subjects = len(student)  # 과목의 수
#     avg = subject_total / subjects
#     print(f"총점 : {subject_total}, 평균 : {avg}")
#
# def main():
#     score = [
#         [88, 76, 92, 98],
#         [65, 70, 58, 82],
#         [82, 80, 78, 88],
#         ]
#
#     total = 0
#     totalsub = 0
#
#     for student in score:
#         subject_total = get_student_score(student)
#
#         print_subject(subject_total, student)
#         subjects = serve_subject(subject_total, student)
#         total += subject_total
#         totalsub += subjects
#
#     total_avg = total / totalsub
#     print(f"전체평균 {total_avg:.2f}")
#
# main()

def findMin(*numbers): # * <- 이 뜻은 가변인수 즉, 갯수의 제한을 두지 않겠다
    min = numbers[0]
    print(numbers)
    for num in numbers: # index[0]부터 loop동작을 실행하겠다
        if num < min:
            min = num
    return min

def findMax(*numbers):
    max = numbers[0]
    print(numbers)
    for num in numbers[1:]: # index[1]부터 index 마지막까지 loop동작을 실행하겠다
        if num > max:
            max = num
    return max

def findMax2(*numbers):
    max(numbers)

    return max

def main():
    min = findMin(2, 7, 5, -1, 20)
    print("최소값 : ", min)

    max = findMax(2, 7, 5, -1, 20)
    print("최대값 : ", max)

    lst = [2, 7, 5, -1, 20]
    max = findMax2(*lst) # * <- 리스트를 벗겨서 내용을 전달해라
    print("최대값 : ", max)

main()
