#include <iostream>
using namespace std;

class Second{
public:
    int sec;

    Second(){
        sec = 0;
    }

    Second(int s){
        sec = s;
    }
};

class Time{
public:
    int hour;
    int minute;
    Second sec;

    // 생성자
    Time() : sec(20) { // Second sec(20); 과 같음
        hour = 0;
        minute = 0;
    }

    // 생성자 overload
    Time(int h, int m) : hour(h), minute(m), sec(20){
    }

    void print(){
        cout << hour << ":" <<minute << endl;
    }
};

void printTime(Time t){ // Time T, call by value Time &T, call by reference, Time *time, call by address
    cout << "Time => " << t.hour << ":" << t.minute << endl;
}

int main(int argc, char const *argv[]) {
    Time a; // 디폴트 생성자를 사용
    Time b(10, 25); // (int, int) 생성자
    Time c; // 정적 객체

    c = b; // 정적 객체(할당)일 때 = 연산은 복사입니다.
    c.hour = 3;

    b.print();
    c.print();

    return 0;
}