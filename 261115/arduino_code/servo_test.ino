
#include <ESP32Servo.h>

#define SERVO_PIN 14
#define POT_PIN 39

Servo myServo;


void setup() {
    myServo.attach(SERVO_PIN);
    pinMode(POT_PIN, INPUT);
}

void loop() {
    int value = analogRead(POT_PIN);
    int mapped_value = map(value, 0, 4095, 0, 180);
    myServo.write(mapped_value);
}
