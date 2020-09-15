#include <LiquidCrystal_I2C.h>
#include <Servo.h>
#include <AnalogSensor.h>
#include <SimpleTimer.h>

AnalogSeneor poten(A0, 0, 180);
// I2C 주소, 칸 수(X), 줄 수(Y)
LiquidCrystal_I2C lcd(0x27, 16, 2);

const int servoPin = 9;
Servo servoMotor;
SimpleTimer timer;

void motorControl(){
    char buf[17];

    int angle = poten.read();
    servoMotor.write(angle);

    sprintf(buf, "angle : %3d", angle);
    lcd.setCursor(0, 0);
    lcd.print(buf);
}

void setup() {
    lcd.init(); // LCD 초기화
    lcd.backlight(); // 백라이트 켜기
    lcd.clear();


    servoMotor.attach(servoPin);
    servoMotor.write(poten.read());
    timer.setInterval(50, motorControl);
    Serial.begin(9600);
}

void loop() {
    timer.run();
}