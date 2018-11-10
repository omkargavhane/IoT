int SLOT1=10;
int SLOT2=11;
int SLOT3=12;
int SLOT4=13;
void setup()
{
  Serial.begin(9600);
  //pinMode(BUZZER,OUTPUT);
  pinMode(SLOT1,INPUT);
  pinMode(SLOT2,INPUT);
  pinMode(SLOT3,INPUT);
  pinMode(SLOT4,INPUT);
  //digitalWrite(SWITCH,HIGH);
  //digitalWrite(BUZZER,LOW);
 
}
void loop()
{
  
  int buttonState=digitalRead(SLOT1);
  if(buttonState==HIGH)
    Serial.print("0");
 
  else
    Serial.print("1");
 buttonState=digitalRead(SLOT2);
  if(buttonState==HIGH)
    Serial.print("0");
 
  else
    Serial.print("1");
 buttonState=digitalRead(SLOT3);
   
  if(buttonState==HIGH)
    Serial.print("0");
 
  else
    Serial.print("1");
  buttonState=digitalRead(SLOT4);
  if(buttonState==HIGH)
    Serial.print("0");
 
  else
    Serial.print("1");
   Serial.println();
   //delay();
}
   //Serial.println("done");
  
