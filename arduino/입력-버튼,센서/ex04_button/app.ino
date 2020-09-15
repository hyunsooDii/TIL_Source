#include <SimpleTimer.h>

SimpleTimer timer;

int pin_LED1 = 4;
int pin_LED2 = 3;
int pin_button = 11;
boolean LED_state = false;


void setup() {
    pinMode(pin_LED1, OUTPUT);
    digitalWrite(pin_LED1, LED_state);
    pinMode(pin_LED2, OUTPUT);
    digitalWrite(pin_LED2, false);

    pinMode(pin_button, INPUT_PULLUP); // 버튼처리할 때 가장 중요!
    timer.setInterval(1000, blink); // 1초 간격으로 블링크, 함수를 매개변수로 참조하는것
}

void blink(){
    LED_state = !LED_state; // 타이머 운영
    digitalWrite(pin_LED1, LED_state); 
}
void loop() {
    timer.run(); 
    // 버튼 상태를 읽어서 13번 핀에 연결된 LED에 표시
    digitalWrite(pin_LED2, !digitalRead(pin_button)); // 풀업이기때문에 부정(!)
}