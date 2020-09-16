#include<DHT.h>
#include <LiquidCrystal_I2C.h>

#define DHTPIN 3
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
    Serial.begin(9600);
    dht.begin();
    lcd.init();
    lcd.backlight();
}

void loop() {
    delay(2000);
    float h = dht.readHumidity(); // 변수 h에 습도 값을 저장
    float t = dht.readTemperature(); // 변수 t에 온도 값을 저장
    char buf[10];

    lcd.home();
    lcd.print("temp: ");
    dtostrf(t, 5, 2, buf);
    lcd.print(buf);
    
    lcd.setCursor(0,1);
    lcd.print("humi: ");
    dtostrf(h, 5, 2, buf);
    lcd.print(buf);
}