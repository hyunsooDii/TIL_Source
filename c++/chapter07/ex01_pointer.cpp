#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
   int number = 0;
   double d = 20.2;

   int *p = &number;
   double *pd = &d;

   cout << p << endl;
   cout << *p << endl;

   cout << sizeof(number) << "," << sizeof(d) << endl;
   cout << sizeof(p) << endl; // int *
   cout << sizeof(pd) << endl; // double *

   return 0;
}