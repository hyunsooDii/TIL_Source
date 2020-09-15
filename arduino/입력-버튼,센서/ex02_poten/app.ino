#include <LiquidCrystal_I2C.h>
#include <PWMLed.h>
#include <AnalogSensor.h>

// I2C 주소, 칸 수(X), 줄 수(Y)
LiquidCrystal_I2C lcd(0x27, 16, 2);

PWMLed led(10);
AnalogSeneor poten(A0, 0, 180);

void setup() {
    Serial.begin(9600);
    lcd.init(); // LCD 초기화
    lcd.backlight(); // 백라이트 켜기
    lcd.setCursor(0,0); // 커서 위치 설정 (x,y)
}

void loop() {
    char buf[17];

    int brightness = poten.read();
    led.set(brightness);

    sprintf(buf, "org : %4d", brightness);
    lcd.setCursor(0, 0);
    lcd.print(buf);

}