#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
   int x, y;
   cout << "input x : ";
   cin >> x;

   cout << "input y : ";
   cin >> y;

   if(x>y){
       cout << "y more than x" << endl;
   } else{
       cout << "x more than y or same" << endl;
   }
   return 0;
}