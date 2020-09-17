#include <SoftwareSerial.h>
#define BT_RXD 2
#define BT_TXD 3

SoftwareSerial softSerial(BT_RXD, BT_TXD);
void setup() {
Serial.begin(9600); // PC 통신
  // 펌웨어로 설정된 디폴트 속도는 115200 bps
  softSerial.begin(9600); // 펌웨어 설정에 따라 조정, ESP와 통신
  softSerial.setTimeout(5000);
  delay(1000);
}
void loop() {
  if (Serial.available()){ // PC로부터 수신 데이터가 있으면
  softSerial.write(Serial.read()); // ESP로 전송
  }
  if (softSerial.available()) { // ESP 모듈로부터 수신 데이터가 있으면
  Serial.write(softSerial.read()); // PC로 전송
  }
}