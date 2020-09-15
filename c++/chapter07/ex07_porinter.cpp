#include <iostream>
#include <string>
using namespace std;

class Dog{
public:
    int age;
    string name;

    Dog(){
        age = 1;
        name = "puppy";
    }    
    ~Dog(){ }

    int getAge() { return age;}
    void setAge(int a) { age = a; } 
};

int main(int argc, char const *argv[]) {
   Dog *pDog = new Dog;

   cout << "puppy's age : " << pDog->getAge() << endl;

   pDog->setAge(3);
   cout << "puppy's age : " << pDog->getAge() << endl;

   delete pDog;
   return 0;
}