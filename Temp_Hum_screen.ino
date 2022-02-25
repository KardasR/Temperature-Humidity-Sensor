#include <dht.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

dht DHT;
LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);

#define DHT11_PIN 2

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  lcd.begin(16, 2);
}

void loop() {
  // put your main code here, to run repeatedly:
  int chk = DHT.read11(DHT11_PIN);
  float temp = (((DHT.temperature) * 1.8) + 32);
  //float raw_temp = DHT.temperature;
  float humid = DHT.humidity;
  lcd.setCursor(0, 0);
  lcd.print("Temp: " + String(temp));
  lcd.setCursor(0, 1);
  lcd.print("Humidity: " + String(humid));
  Serial.print(String(temp) + "|" + String(humid) + "\n");
  delay(10000);
}
