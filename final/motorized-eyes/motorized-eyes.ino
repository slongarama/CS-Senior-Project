#include <ESP32Servo.h>

const byte numChars = 32;
char receivedChars[numChars];
char tempChars[numChars];        // temporary array for use when parsing

// variables to hold the parsed data
char messageFromPC[numChars] = {0};
int xval = 0;
int yval = 0;
float floatFromPC = 0.0;

boolean newData = false;

// servo setup
const int xPin = 18;
const int yPin = 19;
const int x2Pin = 25;
const int y2Pin = 26;
Servo xServo;
Servo yServo;
Servo x2Servo;
Servo y2Servo;

//============

void setup() {
  Serial.begin(9600);
  Serial.println("Enter data in this style <#>  ");
  Serial.println();

  //pins
  xServo.attach(xPin);
  yServo.attach(yPin);
  x2Servo.attach(x2Pin);
  y2Servo.attach(y2Pin);

  //initial positioning
  xServo.write(0);
  yServo.write(0);
  x2Servo.write(0);
  y2Servo.write(0);
}

//============

void loop() {
  recvWithStartEndMarkers();
  if (newData == true) {
    strcpy(tempChars, receivedChars);
    // this temporary copy is necessary to protect the original data
    //   because strtok() used in parseData() replaces the commas with \0
    parseData();
    showParsedData();
    newData = false;
  }
}

//============

void recvWithStartEndMarkers() {
  static boolean recvInProgress = false;
  static byte ndx = 0;
  char startMarker = '<';
  char endMarker = '>';
  char rc;

  while (Serial.available() > 0 && newData == false) {
    rc = Serial.read();

    if (recvInProgress == true) {
      if (rc != endMarker) {
        receivedChars[ndx] = rc;
        ndx++;
        if (ndx >= numChars) {
          ndx = numChars - 1;
        }
      }
      else {
        receivedChars[ndx] = '\0'; // terminate the string
        recvInProgress = false;
        ndx = 0;
        newData = true;
      }
    }

    else if (rc == startMarker) {
      recvInProgress = true;
    }
  }
}

//============

void parseData() {      // split the data into its parts

  char * strtokIndx; // this is used by strtok() as an index
  strtokIndx = strtok(tempChars, ","); // this continues where the previous call left off
  xval = atoi(strtokIndx);     // convert this part to an integer

  strtokIndx = strtok(NULL, ","); // this continues where the previous call left off
  yval = atoi(strtokIndx);     // convert this part to an integer
}

//============

void showParsedData() {
  Serial.print("x ");
  Serial.print(xval);
  Serial.print(" -- y ");
  Serial.println(yval);

  int xco = map(xval, 0 , 600, 140, 40);
  xServo.write(xco);
  x2Servo.write(xco);

  int yco = map(yval, 0 , 333, 40, 140);
  yServo.write(yco);
  y2Servo.write(yco);
}
