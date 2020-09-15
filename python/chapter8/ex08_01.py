# 첨자(인덱스) - 문자열[정수] : 0부터 인덱싱, 문자열[-정수] : 끝에서부터 인덱싱
# 문자열의 떨어져있는 간격 : offset
# len() : 문자열의 길이
# 대표적인 Sequence : 문자열, 리스트, 튜플

# s = "python"
# for c in range(len(s)):
#     print(c, end = ",")

# s = "0123456789"
# print(s[2:5])
# print(s[3:])
# print(s[:4])

# print("2+3 = ", 2+3) # ,와 +의 차이 : ,는 매개변수를 두개 받는 다는 뜻이고 +는 결합한다는 뜻
# print("2+3 = " + "2+3")
#
# file = "20200101-104830.jpg"
# print("촬영 날짜" , file[4:6] , "월" , file[6:8] + "일")
# print("촬영 시간" + file[9:11] + "월" + file[11:13] + "일")
# print("확장자" + file[-3:])

dates = "기러기기러기기러기"
if dates == dates[::-1]:
    print("O")
else:
    print("X")

