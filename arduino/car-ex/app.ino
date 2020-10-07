#include "car.h"

Car car(6, 7, 5, 8, 9, 10);

void setup(){

}

void loop(){
    // 전진
    car.forward();
    delay(2000);

    // 정지
    car.stop();
    delay(2000);

    // 후진
    car.backward();
    delay(2000);   

    // 정지
    car.stop();
    delay(2000);

    // 좌회전
    car.turnLeft();
    delay(2000);

    // 정지
    car.stop();
    delay(2000);

    // 우회전
    car.turnRight();
    delay(2000);

    // 정지
    car.stop();
    delay(2000);
}