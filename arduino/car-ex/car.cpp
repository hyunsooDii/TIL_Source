#include "car.h"

Car::Car(int in1, int in2, int en1, int in3, int in4, int en2):right(in1,in2,en1),left(in3,in4,en2)
{
   
}
    
void Car::forward(int speed){
        right.forward(speed);
        left.forward(speed);
        }
void Car::backward(int speed){
    right.backward(speed);
    left.backward(speed);

}
void Car::turnLeft(int speed){
    right.forward();
    left.backward();
} //r :forward, l: backward
void Car::turnRight(int speed){
    right.backward();
    left.forward();

} //r:backward, l:forward
void Car::setSpeed(int rightSpeed, int leftSpeed){
        right.setSpeed(rightSpeed);
        left.setSpeed(leftSpeed);
}
void Car::stop(){
    right.stop();
    left.stop();
}