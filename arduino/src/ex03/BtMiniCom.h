#pragma once
#include <Arduino.h>
#include <SoftwareSerial.h>
#include <MiniCom.h>

typedef void(*btminicom_callback_t)(String message);

class BtMiniCom : public MiniCom{
protected:
    SoftwareSerial btSerial;
    btminicom_callback_t callback;
public:
    BtMiniCom(int rx, int tx, btminicom_callback_t callback);
    void init();
    String readLine();
    void send(const char *msg);
    void run();

};