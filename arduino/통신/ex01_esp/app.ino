#include <WifiUtil.h>

const char SSID[] = "ABC"; // your network SSID (name)
const char PASSWORD[] = "kim3262286"; // your network password

WifiUtil wifi(2,3); // Rx, Tx

void setup(){
    Serial.begin(9600);
    wifi.init(SSID, PASSWORD);
}

void loop(){
    if(wifi.check()){
        ;
    }
}