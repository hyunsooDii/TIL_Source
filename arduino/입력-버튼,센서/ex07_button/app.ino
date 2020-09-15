#include "Led.h"
#include "Button.h"
#include <SimpleTimer.h>

SimpleTimer timer; // 정적할당, 전역영역

Led led1(3);
Led led2(4);
Led led3(6);

Button btn1(9);
Button btn2(10);
Button btn3(12);

bool blinkPlay = false; // 블링크 중인지 여부, 디폴트는 중지
int blinkTimer = -1; // 블링크용 타이머 ID

void led2OnOff() {
    led2.toggle();
}

void led3Blink(){
    led3.toggle();
}

void led3BlinkControl() {
    blinkPlay = !blinkPlay; // 상태반전
    if(!blinkPlay){ // 이제 블링크 중지면
        led3.off(); 
    }
    timer.toggle(blinkTimer); // 타이머 활성 / 비활성 토글
}

void setup() {
    Serial.begin(9600);
    btn2.setCallback(led2OnOff);
    btn3.setCallback(led3BlinkControl);
    blinkTimer = timer.setInterval(500, led3Blink);
    timer.disable(blinkTimer);
}


// 함수 포인터 형식 : void(*포인터_변수명)(매개변수);

void loop() {
    timer.run();
    led1.set(btn1.read()); // pullup 버튼인 경우 반전
    btn2.check(); // 에지(Falling)가 발생했는지
    btn3.check();
}