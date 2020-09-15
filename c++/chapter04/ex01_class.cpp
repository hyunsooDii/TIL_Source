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
   Circle obj;
   obj.radius = 100;
   obj.color = "blue";
   // obj.area = 40; // 에러 -- 동적으로 멤버 추가 불가

   cout << "circle's radius " << obj.calcArea() << endl;
   return 0;
}