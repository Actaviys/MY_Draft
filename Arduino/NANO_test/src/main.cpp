#include <Arduino.h>

int x; 
void setup() { 
	Serial.begin(115200); 
} 
void loop() { 
	Serial.println("OK"); 
  delay(600);
} 
