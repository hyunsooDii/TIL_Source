int leds[] = {3, 5, 6};

void setup() {
    for(auto &pin_LED: leds){
        pinMode(pin_LED, OUTPUT);
    }
}

void repeat(int pin_LED){
    for(int i=0; i<=255; i++) {
        analogWrite(pin_LED, i);
        delay(10);
    }

    for(int i=255; i>=0; i--){
        analogWrite(pin_LED, i);
        delay(10);
    }
}

void loop() {
    for(auto &pin_LED : leds){
        repeat(pin_LED);
    }
}