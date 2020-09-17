#include <WifiUtil.h>

const char SSID[]="ABC";
const char PASSWORD[]="kim3262286";
const char server[]="arduino.cc";

WifiUtil wifi(2, 3);
WiFiEspClient client;

void request() {
    // if you get a connection, report back via serial
    if (client.connect(server, 80)) { // webserver
        Serial.println("Connected to server");
        // Make a HTTP request
        client.println("GET /asciilogo.txt HTTP/1.1");
        client.println("Host: arduino.cc");
        client.println("Connection: close");
        client.println();
    }
}
void response( ) {
    while (client.available()) {
        char c = client.read();
        Serial.write(c);
    }
}

void setup() {
    Serial.begin(9600);
    wifi.init(SSID, PASSWORD);
    request();
}

void loop() {
    response();
}