// digital
int Led = 13; // define LED Interface
int buttonpin = 3; // define D0 Sensor Interface
int val; // define numeric variables val

void setup() {
    pinMode(Led, OUTPUT); // define LED as output interface
    pinMode(buttonpin, INPUT); // output interface D0 is defined sensor
}
void loop() {
    val = digitalRead(buttonpin);
    if (val == HIGH) {
        digitalWrite(Led, HIGH);
    }
    else {
        digitalWrite(Led, LOW);
    }
}

// // analog
// int sensorPin = A5; // select the input pin for the potentiometer
// int ledPin = 13; // select the pin for the LED
// int sensorValue = 0; // variable to store the value coming from the sensor

// void setup() {
//     pinMode(ledPin, OUTPUT);
//     Serial.begin(9600);
// }
// void loop() {
//     sensorValue = analogRead(sensorPin);
//     digitalWrite(ledPin, HIGH);
//     delay(sensorValue);
//     digitalWrite(ledPin, LOW);
//     delay(sensorValue);
//     Serial.println(sensorValue, DEC);
// }