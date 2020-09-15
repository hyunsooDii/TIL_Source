#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
    int list[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int list2[10];

    // list2 = list <- 문법에러 

    int length = sizeof(list) / sizeof(int); // 40 / 4 => 10

    for(auto i : list2){ // 복사 전 list2 출력
        cout << i << " ";
    }

    for(int i = 0; i < length; i++){ // 값 복사
        list2[i] = list[i];
    }

    for(auto i : list2){ // 복사 후 list2 출력
        cout << i << " ";
    }
    cout << endl;

    return 0;
}