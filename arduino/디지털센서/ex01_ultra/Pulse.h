#pragma once

#include <Arduino.h>

typedef void (*button_callback_t)(int);

class Pulse{
protected :
    int onDelay; // HIGH 시간
    int offDelay; //LOW 시간

    int value; // 현재(H/L) 상태
    unsigned long oldTime; // 최근의 상태 변경 시점 기록
    bool state; // 펄스의 운영 여부
    button_callback_t callback;

public:
    Pulse(int onDelay, int offDelay);
    void setDelay(int onDelay, int offDelay);
    void run();
    int read() { return value; }
    // 간단한 함수는 헤더파일에 정의해도 된다

    bool getState(){ return state; }
    void play();
    void stop();

    void setCallback(button_callback_t callback) { this->callback = callback; }
};