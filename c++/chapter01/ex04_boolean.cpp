#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    bool b;
    b = true;

    cout << b << endl; // 1로 출력됨.

    b = false;
    cout << b;
    return 0;
}