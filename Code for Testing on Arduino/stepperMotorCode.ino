// Pin assignments
const int PUL = 3;   // Step pin
const int DIR = 4;   // Direction pin

void setup() {
  //Set the pinout to output for both Pulse and DIR
  pinMode(PUL, OUTPUT);
  pinMode(DIR, OUTPUT); 

  digitalWrite(DIR, HIGH); // Set direction
}

void loop() {
  // One revolution example (assume 400 steps)
  //Switch Directions
  digitalWrite(DIR, HIGH);
  //send 400 pulses to the motor on each rising edge the motor will set distance.
  for (int i = 0; i < 400; i++) {
    digitalWrite(PUL, HIGH);
    delayMicroseconds(1000);
    digitalWrite(PUL, LOW);
    delayMicroseconds(1000);
  }
  //Switch direction and repeat the previous step
  digitalWrite(DIR, LOW);

  for (int i = 0; i < 400; i++) {
    digitalWrite(PUL, HIGH);
    delayMicroseconds(1000);
    digitalWrite(PUL, LOW);
    delayMicroseconds(1000);
  }
  //create a delay to prevent the motor 
  delay(1000);
}
