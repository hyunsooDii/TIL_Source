#include <LiquidCrystal_I2C.h>
#include <AnalogSensor.h>
#include <Led.h>
#include <PWMLed.h>

AnalogSensor illu(A0, 0, 1023); // 0~100%
LiquidCrystal_I2C lcd(0x27, 16, 2);

// Led led(3);
PWMLed led(3);

void setup() {
    Serial.begin(9600);
    lcd.init();
    lcd.backlight();
    lcd.off();
}

void printIllu(int value){
    char buf[17];
    sprintf(buf, "Read Value = %3d", value);
    lcd.setCursor(0, 0);
    lcd.print(buf);
}

void loop() {
    int readVal = illu.read();
    readVal = constrain(readVal, 0, 200);
    // 값의 범위를 0~200으로 조정, 200이하면 0, 이상이면 200
    // 다른 의미로 센서의 민감도를 조정한 것이다.
    int brightness = map(readVal, 0, 200, 255, 0);
    printIllu(readVal);
    led.set(brightness);
    // if(readVal < 15) { // 어두워지면 LED 켜기
    //     led.on();
    // } else {
    //     led.off();
    // }
    delay(200);
}