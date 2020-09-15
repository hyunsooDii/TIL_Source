#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
   string str;

   do{
       cout<< "input string: ";
       getline(cin, str);
    //    cin >> str;
       cout << "input for user: " << str << endl;
   }while(str != "exit");
   return 0;
}