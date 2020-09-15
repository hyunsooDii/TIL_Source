#include <iostream>
using namespace std;

void f(int i){
    cout << "f(int)" << endl;
}
void f(char *p){
    cout << "f(char *)" << endl;
}

int main(int argc, char const *argv[]) {
   int *pNumber = NULL; // 권장
   int *pNumber2; // 권장하지 않음

   if(pNumber != NULL){ // 포인터의 안전성을 고려하여
       cout << *pNumber << endl;
   }

   if(pNumber2 != NULL){
       cout << *pNumber2 << endl;
   }

   // f(NULL); // -- int, char * 둘 다 가능하므로 에러, NULL - 숫자 0
   f(nullptr); // nullptr : 포인터 NULL -> f(char *)
   f(0); // 숫자 0 -> f(int)
   return 0;
}