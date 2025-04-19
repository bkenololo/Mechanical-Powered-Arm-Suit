#include <Servo.h>
Servo myServo;

int pos = 90; // Posisi awal default

void setup() {
  Serial.begin(9600);
  myServo.attach(9); // Ganti pin sesuai servo kamu
  myServo.write(pos);

  Serial.println("Atur posisi awal servo (0 - 180):");
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n'); // Baca input sampai enter
    int newPos = input.toInt(); // Ubah ke angka

    if (newPos >= 0 && newPos <= 180) {
      pos = newPos;
      myServo.write(pos);
      Serial.print("Servo dipindah ke: ");
      Serial.println(pos);
    } else {
      Serial.println("Masukkan angka antara 0 - 180.");
    }
  }
}
