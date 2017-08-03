#include <LiquidCrystal.h>

LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

int counter = 1;

void setup() {
  Serial.begin(9600);

  lcd.begin(16, 2);
  lcd.clear();
  lcd.print("   <ETHEREUM>");
}

void loop() {

  if(counter==1){
    Serial.println("Arduino Activated!");
    delay(1000);
    counter++;
  }

  delay(1000);

  while(Serial.available()){
    delay(30);
    String printl = Serial.readStringUntil('\n');
    Serial.println(printl);
    lcd.clear();
    lcd.print("   <ETHEREUM>");
    lcd.setCursor(0, 1);
    lcd.print(printl);
    delay(1000);
    counter++;
  }

}