//capstone 2021/2022

#include <SoftwareSerial.h>

//define pin numbers for steps and direction
const int stpPin=2; //digital pin 2
const int dirPin=3; //digital pin 3


String incomingByte;
float separation;
int i=0;

//stage displacement (mm)
int initpos=26; //input initial position
int desiredpos; //input desired position

//no. motor rotations
float inita1; 
float desireda1;
float inita; 
float desireda;
float deltaa; //number rotations required

//number of steps
float nostep;


void setup() {
  //Serial.begin(9600);
  
  //define the pins as outputs
  pinMode (stpPin,OUTPUT);
  pinMode (dirPin,OUTPUT);

  Serial.begin(9600);
  
}

void loop() {

  initpos=initpos;
  if(Serial.available() > 0){
    while (Serial.available() > 0)  //See if data is there
    {
      incomingByte= Serial.readString();  //Read a byte
      delay(50);
      desiredpos=incomingByte.toInt();
      Serial.println(desiredpos);
    } 

  inita1=pow(initpos, 2.8207796311);
  inita=0.0001878373*inita1;
  desireda1=pow(desiredpos, 2.8207796311);
  desireda=0.0001878373*desireda1;

 //inita=(0.0088*(pow(initpos, 2)))-(0.3675*initpos)+3.9582; //calc init no. step using formula
  inita=(0.0088*(pow(initpos, 2)))-(0.3675*desiredpos)+3.9582;
  desireda=(0.0088*(pow(desiredpos, 2)))-(0.3675*desiredpos)+3.9582; //calc desired no. step using formula
  
  deltaa=desireda-inita;
  nostep=abs(deltaa)*200;
  
  //set direction
  if (deltaa >= 0) {
   digitalWrite(dirPin,HIGH); //raise stage
  }
  else {
    digitalWrite(dirPin,LOW); //lower stage
  }
  
  //for one full rotation - 200 steps/pulses (1.8 deg step angle)
  for(int x=0; x < nostep; x++) {
    digitalWrite(stpPin,HIGH);
    //speed of motor depends on delay time)
    delayMicroseconds(1000);
    digitalWrite(stpPin,LOW);
    delayMicroseconds(1000);
  }
 }
 initpos=desiredpos;
 delay(1000);

//after execution unplug the power supply
 
}
