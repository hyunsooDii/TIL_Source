# 파일

# 파일 입출력

# 파일 쓰기 - open(파일경로, 모드)

import pickle

# def main():
#     f = open("live.txt", "wt", encoding="utf8")
#     f.write("""가나다라마바사아자차카타파하
# 믿으라, 기쁨의 날이 오리니
# """)
#
#     f.write("""삶이 그대를 속일지라도
# 슬퍼하거나 노하지 말라!
# 우울한 날들을 견디면
# 믿으라, 기쁨의 날이 오리니
# """)
#
#     f.close()
#     f = open("live.txt", "at", encoding="utf8")
#     f.write("""가나다라마바사아자차카타파하
# 믿으라, 기쁨의 날이 오리니
# """)
#     f.close()

# 파일 읽기

#     try:
#         fl = open("test1/t.txt", "rt", encoding="utf8")
#         text = fl.read()
#         print(text)
#     except FileNotFoundError:
#         print("파일이 없습니다.")
#     finally:
#         fl.close()
#
# main()

# def main():
#     f = open("live.txt", "rt", encoding="utf8")
#
#     while True:
#         text = f.read(10)
#         if len(text) == 0: break
#         print(text, end="")
#
#     f.close()
#
# main()

# def main():
#     f = open("live.txt", "rt", encoding="utf8")
#     text = ""
#     line = 1
#     while True:
#         row = f.readline() # readline 함수는 binary 파일에서는 사용할 수 없음, 즉 문자열, 비어있는 문자열일 때 False
#         if not row: break
#         text += str(line) + " : " + row
#         line += 1
#
#     f.close()
#     print(text)
#
# main()

# def main():
#     f = open("live.txt", "rt", encoding="utf8")
#     rows = f.readlines()
#
#     for ix, row in enumerate(rows, 1):
#         print(f"{ix} : {row}", end="")
#
#     f.close()
#
# main()

# def save(fpath, data):
#     try:
#         with open(fpath, "wt") as file:
#             for l in data:
#                 row = ','.join(map(str, l))
#                 file.write(row + "\n")
#     except Exception:
#         print("파일이 없습니다.")
#
# def load(fpath):
#     try:
#         with open(fpath, "rt") as file:
#             lines = file.readlines()
#             data = []
#             for line in lines:
#                 print(line, end='')
#                 row = line.split(',') # split 메소드 - 리스트로 변경됨
#                 print(row)
#                 row = list(map(int, row)) # 문자열을 int형으로 변환
#                 print(row)
#                 data.append(row)
#     except Exception:
#         print("파일이 없습니다.")
#
#     return data
#
#
# def main():
#     data = [
#         [1, 2, 3, 54, 45],
#         [7, 8, 3, 4, 5],
#         [1, 12, 13, 4, 25]
#     ]
#
#     save("data.csv", data)
#     load("data.csv")
#
#
# main()

# 입출력 위치 - seek(위치, 기준) 거의 binary모드에서 사용

# def main():
#     f = open("live.txt", "rt", encoding="utf8")
#
#     f.seek(0, 1)
#     text = f.read()
#     f.close()
#
#     print(text)
#
# main()

# 내용 추가
# w모드 - 기존에 파일이 존재하는 경우 내용을 모두 지우고 다시 작성
# a모드 - 기존에 파일이 존재하는 경우 파일의 끝에 내용을 추가

# def main():
#     f = open("live.txt", "at", encoding="utf8")
#     f.write("\n\n푸쉬킨 형님의 말씀")
#
#     text = f.read()
#     print(text)
#
#     f.close()
# main()

# with ~ as문 - open() 함수와 함께 사용하면 명시적으로 close함수를 호출하지 않아도 파일이 항상 닫힘

# def main():
#     try:
#         with open("live.txt", "r", encoding="utf8") as file:
#             text = file.read()
#             print(text)
#     except FileNotFoundError:
#         print("파일이 없습니다")
#
# main()

# pickle 모듈 - 파이썬 자료형 그대로 저장하고, 그대로 복원, 반드시 binary 모드로 오픈해야 함, 다른 언어와 호환성 x

def save(fpath, data):
    try:
        with open(fpath, "wb") as file:
            pickle.dump(data, file)
    except Exception as e:
        print(f"{fpath} 파일 쓰기에 실패했습니다.")
        print(e)

def load(fpath):
    try:
        with open(fpath, "rb") as file:
            data = pickle.load(file)
            return data
    except Exception as e:
        print(f"{fpath} 파일 읽기에 실패했습니다.")
        print(e)

def main():
    data = [
        [1, 2, 3, 54, 45],
        [7, 8, 3, 4, 5],
        [1, 12, 13, 4, 25]
    ]

    save("./data/data2.dat", data)
    data2 = load("./data/data2.dat")
    print(data2)


main()
