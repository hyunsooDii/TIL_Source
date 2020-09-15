# data 관리하는 class
# model class 라고도 불림

class Addr:
    def __init__(self, name, phone, addr):
        self.name = name
        self.phone = phone
        self.addr = addr

    def __str__(self):
        return f"<Addr {self.name}/{self.phone}/{self.addr}>"

    def __repr__(self):
        return f"<Addr {self.name}>"