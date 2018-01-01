
int recdata = 0;
int inte = 0;
#include <Servo.h>
Servo pro;
int spin = 9;





void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  pro.attach(9);
  
  }

void loop() {
  if (Serial.available() > 0){
    recdata = Serial.read();
    Serial.println(recdata);
    if (recdata == 49){
      digitalWrite(13,HIGH);
      pro.write(180);
      delay(100);
    }
    else if (recdata = 48){
      digitalWrite(13,LOW);
      pro.write(0);
      delay(100);
      
    }
    
     
  }
  

}
