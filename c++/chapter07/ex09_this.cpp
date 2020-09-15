#include <iostream>
#include <string>
using namespace std;

class Rectangle{
private:
    int length;
    int width;
public:
    // Rectangle(int length=30, int width=40){
    //     this->length = length;
    //     this->width = width;
    // }    

    // 멤버 초기화 리스트로 초기화하기
    Rectangle(int length=30, int width=40) : length(length), width(width){
    }
    ~Rectangle() {}
    void setLength(int length){
        this->length = length;
    }
    int getLength(){
        return this->length;
    }
    void setWidth(int width){
        this->width = width;
    }
    int getWidth(){
        return this->width;
    }
};

int main(int argc, char const *argv[]) {
   Rectangle rect;

   cout << "rectangle's width : " << rect.getWidth() << endl;
   cout << "rectangle's length : " << rect.getLength() << endl;

   rect.setLength(50);
   rect.setWidth(60);

   cout << "rectangle's width : " << rect.getWidth() << endl;
   cout << "rectangle's length : " << rect.getLength() << endl;
   return 0;
}