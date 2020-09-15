#include <string.h>
#include <iostream>
using namespace std;

class MyString{
private:
    char *s;
    int size;

public:
    MyString(char *c){
        size = strlen(c) + 1;
        s = new char[size];
        strcpy(s, c);
    }
    
    ~MyString(){
        cout << "~Mystring ... delete s" << endl;
        delete[]s;
    }
};

int main(int argc, char const *argv[]) {
   MyString str("abcdefghijk");

   return 0;
}