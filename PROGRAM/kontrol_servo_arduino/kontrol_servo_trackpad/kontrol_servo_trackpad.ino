#include <Servo.h>
Servo myServo;

int pos = 90;

void setup() {
  Serial.begin(9600);
  myServo.attach(9);
  myServo.write(pos);
}

void loop() {
  if (Serial.available()) {
    while (Serial.available()) {
      char command = Serial.read();

      if (command == 'R') {
        pos += 3;
      } else if (command == 'L') {
        pos -= 3;
      } else if (command == 'S') {
        // stop, ignore or use logic if needed
      }
    }

    pos = constrain(pos, 0, 180);
    myServo.write(pos);
  }
}
