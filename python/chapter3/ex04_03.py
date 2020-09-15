a = 3
if a == 3 :
    print("3이다")

if a > 5 :
    print("5보다 크다")

if a < 5 :
    print("5보다 작다")

# 컴퓨터는 비교연산을 실행할 때 두 값의 차이 연산을 하며 비교를 한다. <- 알고리즘 응용

if "Korea" < "korea" :
    print("소문자가 더 큼")

s1 = "K"
s2 = "k"
print(ord(s1))
print(ord(s2))

print(bool(None))
print(bool(0))
print(bool(""))
print(bool([]))
print(bool(()))

if 1 < a < 10 :
    print("OK")

age = 25
if age < 19 :
    print("애들은 가라")
    print("공부 열심히 하세요")

else :
    print("들어오세요")
    print("즐거운 시간 되세요")

age = 23
if age < 19 :
    print("애들은 가라")

elif age < 25 :
    print("대학생입니다")

else :
    print("들어오세요")

score = 80

if (score <= 100 and score > 90) :
    print("A학점")
elif (score <= 90 and score > 80) :
    print("B학점")
elif (score <= 80 and score > 70) :
    print("C학점")
elif (score <= 70 and score > 60) :
    print("D학점")
else :
    print("F학점")

age = 26
if age < 19 :
    print("애들은 가라")
else :
    if age < 25 :
        print("대학생입니다.")
    else :
        print("들어오세요")

man = True
age = 22

if man == True :
    if age > 19 :
        print("성인 남자 입니다.")
    else :
        print("미성년 남자 입니다")
else :
    if age > 19 :
        print("성인 여자 입니다")
    else :
        print("미성년 여자 입니다")