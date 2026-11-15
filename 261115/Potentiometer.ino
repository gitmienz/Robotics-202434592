const int potPin = A2;
const int ledPin = 9;

void setup()
{
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);
}

void loop()
{
  int value = analogRead(potPin);
  Serial.println(value);
  
  value = value/1023*255;
  //map(value, 0, 1023, 0, 255)
  
  analogWrite(ledPin, value);
  
  delay(50);
}
