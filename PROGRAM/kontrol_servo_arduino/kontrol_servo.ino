#include <Servo.h>

Servo myServo;
int pos = 90;

void setup() {
  myServo.attach(9);
  myServo.write(pos);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char cmd = Serial.read();
    if (cmd == 'L') {
      pos = constrain(pos - 2, 0, 180);
    } else if (cmd == 'R') {
      pos = constrain(pos + 2, 0, 180);
    }
    myServo.write(pos);
  }
}
