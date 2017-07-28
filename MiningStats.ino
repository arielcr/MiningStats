#include <LiquidCrystal.h>

LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

int counter = 1;

void setup() {
  Serial.begin(9600);

  lcd.begin(16, 2);
  lcd.clear();
  lcd.print(".:Mining Stats:.");
}

void loop() {

  if(counter==1){
    Serial.println("Arduino Activado");
    delay(1000);
    counter++;
  }

  delay(1000);

  while(Serial.available()){
    delay(30);
    if(counter==2){
      String printl = Serial.readStringUntil('\n');
      Serial.println(printl);
      lcd.clear();
      lcd.print(printl);
      delay(1000);
      counter++;
    }
  }

}
