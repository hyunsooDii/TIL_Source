#include <iostream>
using namespace std;

void initArray(int array[], int size, int value=0){
    for(int i=0; i<size; i++){
        array[i] = value;
    }
}

void printArray(int array[], int size){
    for(int i=0; i<size; i++){
        cout << array[i] << ", ";
    }
    cout << endl;
}

int main(int argc, char const *argv[]) {
   int intList[10];

   initArray(intList, 10, 100);
   printArray(intList, 10);

   initArray(intList, 10);
   printArray(intList, 10);
   return 0;
}