#include <iostream>
#include <string>
using namespace std;

int main(int argc, char const *argv[]) {
   string s1, addr;

   cout << "input name : ";
   cin >> s1;
   cin.ignore(); // 엔터키 제거

   cout << "input address : ";
   getline(cin, addr); // enter칠 때까지 입력을 받아달라
   
   cout << addr << " to " << s1 << " hello ? " << endl;
   return 0;
}