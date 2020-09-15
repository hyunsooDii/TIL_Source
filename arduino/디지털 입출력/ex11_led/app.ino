#include <SimpleTimer.h>

int pin_LED1 = 3;
int pin_LED2 = 5;
int pin_LED3 = 7;
SimpleTimer timer;

void blink_1000(){
    int state = digitalRead(pin_LED1); // 지정한 핀의 현재 상태 읽기
    digitalWrite(pin_LED1, !state);
}

void blink_500(){
    int state = digitalRead(pin_LED2);
    digitalWrite(pin_LED2, !state);
}

void blink_200(){
    int state = digitalRead(pin_LED3);
    digitalWrite(pin_LED3, !state);
}

void setup(){
    pinMode(pin_LED1, OUTPUT);
    pinMode(pin_LED2, OUTPUT);
    pinMode(pin_LED3, OUTPUT);
    timer.setInterval(1000, blink_1000);
    timer.setInterval(500, blink_500);
    timer.setInterval(200, blink_200);
}

void loop(){
    timer.run();
}

// boolean LED_state1 = false;
// unsigned long time_previous1, time_current1;

// boolean LED_state2 = false;
// unsigned long time_previous2, time_current2;

// unsigned long count = 0;

// void setup() {
//     pinMode(pin_LED1, OUTPUT);
//     pinMode(pin_LED2, OUTPUT);
//     digitalWrite(pin_LED1, LOW);
//     digitalWrite(pin_LED2, LOW);
//     Serial.begin(9600);
//     time_previous1 = millis();
//     time_previous2 = millis();

// }


// void loop(){
//     blink_1000();
//     blink_500();
// }

// void blink_1000() {
//     time_current1 = millis();
//     // 1초 이상 시간이 경과한 경우
//     if(time_current1 - time_previous1 >= 1000) {
//         time_previous1 = time_current1; //  // 1초가 지나고 time_previous를 현재 시간으로 바꿔줌
//         LED_state1 = !LED_state1;
//         digitalWrite(pin_LED1, LED_state1);
//     }
// }

// void blink_500() {
//     time_current2 = millis();
//     // 0.5초 이상 시간이 경과한 경우
//     if(time_current2 - time_previous2 >= 500) {
//         time_previous2 = time_current2;
//         LED_state2 = !LED_state2;
//         digitalWrite(pin_LED2, LED_state2);
//     }
// }