const int ledPin = 7;
const int buttonPin = 2;
int isButton = 0;
 

void setup()
{
  pinMode(buttonPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop()
{
  int buttonState = digitalRead(buttonPin);

  if(buttonState == HIGH){
    
    if (isButton == 0){
      isButton = 1;
    }
    else if (isButton == 1) {
      isButton = 0;
    }
  }
  
  if(isButton == 1)
  {
    digitalWrite(ledPin, HIGH);
  }
  else if (isButton == 0)
  {
    digitalWrite(ledPin, LOW);
  }

  
}
