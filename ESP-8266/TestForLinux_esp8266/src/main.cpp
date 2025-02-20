#include <Arduino.h>

#define LED1 4


void setup() {
  Serial.begin(115200);
  pinMode(LED1, OUTPUT);
}

void loop() {
  Serial.println("Ok");
  digitalWrite(LED1, 1);
  delay(600);

}


