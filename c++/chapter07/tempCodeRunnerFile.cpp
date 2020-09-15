#include <iostream>
using namespace std;

void print(string t){
    cout << t << endl;
}

int main(int argc, char const *argv[]) {
    
   char test[] = "Hello";
   char *pstr = "C++";
   string str = "World";

   // *pstr = 'P'; // 에러남
   print(test);
   print(pstr);
   print(str);
   return 0;
}