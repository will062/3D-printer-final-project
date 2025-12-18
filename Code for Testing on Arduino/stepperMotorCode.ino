// Pin assignments
const int PUL = 3;   // Step pin
const int DIR = 4;   // Direction pin

void setup() {
  pinMode(PUL, OUTPUT);
  pinMode(DIR, OUTPUT);

  digitalWrite(DIR, HIGH); // Set direction
}

void loop() {
  // One revolution example (assume 200 steps)
  digitalWrite(DIR, HIGH);

  for (int i = 0; i < 400; i++) {
    digitalWrite(PUL, HIGH);
    delayMicroseconds(1000);
    digitalWrite(PUL, LOW);
    delayMicroseconds(1000);
  }

  digitalWrite(DIR, LOW);

  for (int i = 0; i < 400; i++) {
    digitalWrite(PUL, HIGH);
    delayMicroseconds(1000);
    digitalWrite(PUL, LOW);
    delayMicroseconds(1000);
  }
  delay(1000);
}
