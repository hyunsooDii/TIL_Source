# 사전 - 두 개의 정보를 짝을 지어서 관리 (key->중복된 값x 유일해야 함, value)
# 키와 값의 쌍으로 관리되는 데이터, 다른 언어에서는 map이라함
# 사전은 순서(인덱스)가 없다

# def main():
#     dic = {
#         'boy' : '소년',
#         'school' : '학교',
#         'book' : '책'
#     }
#     print(dic)
#
# main()

# def main():
#     dic = { 'boy' : '소년', 'school' : '학교', 'book' : '책'}
#     name = 'boy'
#     print(dic[name])
#     print(dic['school'])
#     print(dic['girl'])
#
# main()

# def main():
#     dic = {'boy': '소년', 'school': '학교', 'book': '책'}
#     print(dic.get('boy'))
#     print(dic.get('girl'))
#     print(dic.get('girl', '사전에 없는 단어입니다.'))
#
# main()

# def main():
#     dic = {'boy': '소년', 'school': '학교', 'book': '책'}
#     if 'student' in dic:
#         print("사전에 있는 단어 입니다.")
#     else:
#         print("이 단어는 사전에 없습니다.")
#
# main()

# def main():
#      dic = {'boy': '소년', 'school': '학교', 'book': '책'}
#      dic['boy'] = '남자아이'
#      dic['girl'] = '소녀'
#      print(dic)
#
# main()

# def main():
#     dic = {'boy': '소년', 'school': '학교', 'book': '책'}
#     keylist = dic.keys()
#     for key in keylist:
#         print(key, dic[key])
#
#     li = list(dic.keys())
#     print(li)
#
#     li = list(dic)
#     print(li)
#
# main()

# def main():
#     dic = {'boy': '소년', 'school': '학교', 'book': '책'}
#     dic2 = {'student' : '학생', 'teacher' : '선생님', 'book' : '서적'}
#     # 두 dictionary를 합칠 때, 같은 key값이 있으면 그대로 붙여버림
#     dic.update(dic2)
#     print(dic)
#
# main()

# def main():
#     li = [
#         ['boy','소년'],
#         ['school','학교'],
#         ['teacher', '선생님']
#     ]
#     # 리스트나 튜플을 dictionary 로 변환할 때, 한 행에 key와 value값만 포함되어야 함
#     dic = dict(li)
#     print(dic)
#
# main()
# users = {
#     "go": "g1234",
#     "hong": "h1234"
# }
#
# def get_user_info():
#     user_id = input("사용자 ID : ")
#     password = input("비밀번호 : ")
#
#     return user_id, password
#
# def check_login(user_id, password):
#     if user_id not in users:
#         print(f"{user_id}는 존재하지 않는 ID입니다. ")
#         return False
#     elif users[user_id] == password:
#         return True
#     else:
#         print("비밀번호가 틀렸습니다")
#         return False
#
# def print_result(result, user_id):
#     if result:
#         print(f"로그인에 성공했습니다. 반갑습니다. {user_id}님")
#     else:
#         print("로그인에 실패했습니다. \n다음기회에...")
#
# def main():
#     user = dict()

    # for i in range(4):
    #     id = input("ID를 입력하세요 ")
    #     pw = input("비밀번호를 입력하세요 ")
    #     if user.get(id) == pw:
    #         print(f"로그인 성공, 반갑습니다 {user.get(id)}님")
    #         break
    #     else:
    #         print("로그인 실패")

    # cnt = 0
    #
    # for key, value in user.items():
    #     if cnt == 2:
    #         print("로그인횟수 3회초과, 프로그램 종료")
    #         break
    #     id = input("ID를 입력하세요 : ")
    #     if key != id:
    #         print("ID 다시 입력 ")
    #         cnt += 1
    #     elif key == id:
    #         pw = input("PW를 입력하세요 : ")
    #         if (value == pw):
    #             print(f"로그인 성공, 반갑습니다 {id}님")
    #         else:
    #             print("로그인 실패")
    #             cnt +=1

#     result = False
#
#     for i in range(3):
#         user_id, password = get_user_info()
#         result = check_login(user_id, password)
#         if result:
#             break
#
#     print_result(result,user_id)
#
# main()

def main():
    song = """by the rivers of babylon, there we sat down
    yeah we wept, when we remember zion.
    when the wicked carried us away in captivity
    required from us a song
    now how shall we sing the lord's song in a strange land"""

    alphabet = dict()
    for c in song:
        if c.isalpha() == False:
            continue

        c = c.lower()
        if c not in alphabet:
            alphabet[c] = 1
        else:
            alphabet[c] += 1

    print(alphabet)

    key = list(alphabet.keys())
    key.sort()
    for c in key:
        num = alphabet[c]
        print(c, '=>', num)

main()

