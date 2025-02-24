#include <Arduino.h>

#define LEDred 5
#define LEDgreen 4

String inBytes;

void setup() {
  Serial.begin(115200);
  pinMode(LEDred, OUTPUT);
  pinMode(LEDgreen, OUTPUT);

  // digitalWrite(LEDgreen, 1);
  // digitalWrite(LEDred, 1);
}

void loop() {
  if (Serial.available() > 0 ){
    inBytes = Serial.readStringUntil('\n');
    if (inBytes == "LedGreen,1"){ // Led Green
      digitalWrite(LEDgreen, 1);
      Serial.print("ret. disp. - ");
      Serial.println(inBytes);
    }
    if (inBytes == "LedGreen,0"){
      digitalWrite(LEDgreen, 0);
      Serial.print("ret. disp. - ");
      Serial.println(inBytes);
    }

    if (inBytes == "LedRed,1"){ // Led Red
      digitalWrite(LEDred, 1);
      Serial.print("ret. disp. - ");
      Serial.println(inBytes);
    }
    if (inBytes == "LedRed,0"){
      digitalWrite(LEDred, 0);
      Serial.print("ret. disp. - ");
      Serial.println(inBytes);
    }

    if (inBytes == "Display"){ // Display
      Serial.print("ret. disp. - ");
      Serial.println(inBytes);
    }
    
  }


  

}


