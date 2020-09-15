a = "I Say \"Hello\" to you"
print(a)
a = "I Say \'Hello\' to you"
print(a)

a = 'first\rsecond'
print(a)

a = 'first\tsecond'
print(a)

linecontinue = 365 * 24 * \
               60 * 60
print(linecontinue)

s = "korea" "japan" "2002"
print(s)

s = ("korea"
     "japan"
     "2002")
print(s)

print(ord('a'))
print(chr(98))

for c in range(ord('A'), ord('Z')+1): # 아스키 코드 바꾸는거
    print(chr(c),chr(c) , sep = '^^', end = ' ')

print()
a = 5
b = (a == 5)
print(type(b))
print(b)

member = ['손오공', '저팔계', '사오정', '삼장법사']
print(type(member))
print(member[2])

member = ('손오공', '저팔계', '사오정', '삼장법사') # List와 Tuple 차이점 : List은 리터널로 []사용, Tuple은 ()사용,
                                                #  List는 읽기와 쓰기 가능, Tuple은 읽기 전용
print(type(member))
print(member[1])
print(member[0])