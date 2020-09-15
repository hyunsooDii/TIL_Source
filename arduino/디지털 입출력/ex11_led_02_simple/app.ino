#include <SimpleTimer.h>

SimpleTimer timer; // 정적할당, 전역영역

void printTest(){
    Serial.println("simple call by 1 sec");
}

void printTest2(){
    Serial.println("simple call by 0.5 sec");
}

void setup(){
    Serial.begin(9600);
    timer.setInterval(1000, printTest);
    timer.setInterval(500, printTest2);
}

void loop(){
    timer.run();
}