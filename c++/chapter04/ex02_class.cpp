#include <iostream>
using namespace std;

class Circle{
public:
    int radius; // 반지름
    string color; // 색상

    double calcArea(){ // python과 달리 self 매개 변수 없음
        return 3.14 * radius * radius; // 멤버 변수 접근 시 바로 사용
    }
};

int main(int argc, char const *argv[]) {
   Circle pizza1, pizza2; // 객체 생성, 정적할당

   pizza1.radius = 100;
   pizza1.color = "yellow";
   cout << "pizza's radius " << pizza1.calcArea() << endl;

   pizza2.radius = 200;
   pizza2.color = "white";
   cout << "pizza's radius " << pizza2.calcArea() << endl;  
   return 0;
}