# 컬렉션 관리 함수 - enumerate

# def main():
#     score = [88, 95, 70, 100, 99]
#
#     for no, sco in enumerate(score, 1):
#         print(str(no) + "번 학생 성적 : ", sco)
#
#     race = ['저그', '테란', '프로토스']
#     print(list(enumerate(race)))
#     print(race)
#
# main()

# zip - 하나로 묶는거, 동일 index 의 element 를 묶는다. 만약 시퀀스의 길이가 다른 경우 짧은 시퀀스의 길이에 맞춤

# def main():
#     dates = ['월', '화', '수', '목', '금', '토', '일']
#     food = ["갈비탕", "순대국", "칼국수", "삼겹살"]
#     price = [5000, 6000, 4000, 8000]
#
#     menu_dic = dict(zip(dates, food))
#     print(menu_dic)
#
#
# main()

# 단어 조합 변수명 표기법
# 1. SalesRate, MenuDic, PrintAverage -> Pascal case (클래스 이름)
# 2. sales_rate, Menu_dic, print_average -> Snake case (c/c++ 언어에서 씀)
# 3. salesRate, menuDic, printAverage -> Camel case (Java 언어에서 씀)
# 4. sales-rate-, menu-dic-, print-average- Kebab case (Tag 언어에서 씀(HTML))

# any(), all() 함수 - 시쿼스에 하나(any)라도 True가 있으면 True, 시퀀스의 모든 요소가 True 이면 True(all)

# def main():
#     adult = [True, False, True, False]
#     print(any(adult))
#     print(all(adult))
#
# main()