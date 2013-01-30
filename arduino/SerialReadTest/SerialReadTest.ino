//This code will flash the LED on pin 13 the numbers of times matching the
//int sent via serial. i.e. if the number 6 is sent the LED will flash 6 times.

int ledPin =  13;      

void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);  
  Serial.begin(9600);  

}

void loop(){

}

void serialEvent() {

  int incoming = Serial.read();
  int amount = incoming - 20;
  
  incoming = 0;

  for(int i = 0; i < amount; i++) {

    flash();
  }
  
  amount = 0;

}


void flash()
{

  digitalWrite(ledPin, HIGH);
  delay(100);
  digitalWrite(ledPin, LOW);
  delay(100);
  
  delay(1000);

}


