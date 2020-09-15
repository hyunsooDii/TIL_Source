#include <iostream>
#include <string>
using namespace std;

int main(int argc, char const *argv[]) {
    int x = 100;
    int y = 200;

    int result = x + y;
    cout << "x + y : " << result << endl;
    cout << "x- y : " << x- y << endl;
    cout << "x / y : " << x /y << endl;
    cout << "x / y : " << x /(double)y << endl; // type cast
    cout << "x % 3 : " << x % 3 << endl;
    cout << 1/2 << endl; // 정수/정수 --> 정수(몫)
    cout << 1/2. << endl; // 정수/실수 --> 실수, 좀 더 범위가 넓은걸로 반환
    return 0;
}