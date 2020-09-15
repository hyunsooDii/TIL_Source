# 메모장

import sys
from myapp import Application, MenuItem

class NotepadApp(Application):
    def __init__(self):
        super().__init__()

    def create_menu(self, menu):
        menu.add(MenuItem("열기", self.open()))
        menu.add(MenuItem("저장", self.save()))
        menu.add(MenuItem("목록보기", self.print_list()))
        menu.add(MenuItem("종료", self.exit()))

    def open(self):
        print("열기를 실행합니다.")

    def save(self):
        print("저장을 실행합니다.")

    def print_list(self):
        print("목록 보기를 실행합니다.")

    def exit(self):
        sys.exit(0)

class AddressBookApp(Application):
    pass


def main():
    app = NotepadApp()
    app.run

if __name__ == "__main__":
    main()

# menu = Menu()
# item = MenuItem("열기", Application.open())
# menu.add(item)
# menu.add(MenuItem("저장", lambda :print("저장 실행")))
# menu.add(MenuItem("목록보기", lambda :print("목록보기 실행")))
# menu.add(MenuItem("종료", lambda :print("종료 실행")))
# menu.print()
# menu.run(1) # 저장 메뉴 실행
# menu.run(3) # 종료 메뉴 실행
# menu.run(4) # 잘못된 메뉴


