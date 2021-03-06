int ledPin = 13;
int inputPin = 7;
int pirState = LOW;
int val = 0;

void setup(){
    pinMode(ledPin, OUTPUT);
    pinMode(inputPin, INPUT);
    Serial.begin(9600);
}

void loop(){
    val = digitalRead(inputPin);
    if(val == HIGH){
        digitalWrite(ledPin, HIGH);
        if(pirState == LOW){ // 첫번째 감지에서만 처리
            Serial.println("Motion detected!");
            pirState = HIGH;
        }
        else {
            digitalWrite(ledPin, LOW);
            if(pirState == HIGH){ // 첫번째 감지시에만 처리
                Serial.println("Motion ended!");
                pirState = LOW;
            }
        }
    }
}