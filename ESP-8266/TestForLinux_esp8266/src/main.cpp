#include <Arduino.h>

#define LEDred 5
#define LEDgreen 4

String inBytes;

void setup() {
  Serial.begin(115200);
  pinMode(LEDred, OUTPUT);
  pinMode(LEDgreen, OUTPUT);
}

void loop() {
  if (Serial.available() > 0 ){
    inBytes = Serial.readStringUntil('\n');
    if (inBytes == "on"){
      digitalWrite(LEDgreen, 1);
    }
    if (inBytes == "off"){
      digitalWrite(LEDgreen, 0);
    }
  }
  // Serial.println("Ok");
  // digitalWrite(LEDred, 1);
  // digitalWrite(LEDgreen, 0);
  // delay(600);

}


