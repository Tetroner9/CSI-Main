#include <Arduino.h>

const int inputPins[] = {12, 13, 14, 27, 26};
const int relayPins[] = {19, 21, 22, 23};
const int sequence[] = {12, 13, 14, 27};
const int sequenceLength = 4;

bool ledsActive[] = {false, false, false, false};

int sequenceIndex = 0;
bool ledsOn = false;
int lastButtonPressed = -1;

void setup() {
  for (int i = 0; i < 4; i++) {
    pinMode(inputPins[i], INPUT_PULLUP);
    pinMode(relayPins[i], OUTPUT);
    digitalWrite(relayPins[i], LOW);
  }
  pinMode(inputPins[4], INPUT_PULLUP);
  Serial.begin(115200);
}

void loop() {
  if (digitalRead(inputPins[4]) == LOW) {
    resetGame();
  } else {
    checkSequence();
    if (sequenceIndex == sequenceLength && !ledsOn) {
      activateAllRelays();
      ledsOn = true;
    }
  }
  delay(100);
}

void checkSequence() {
  if (sequenceIndex < 0 || sequenceIndex >= sequenceLength) {
    return;
  }

  int buttonPressed = findPressedButton();
  
  if (buttonPressed != -1 && buttonPressed == sequence[sequenceIndex]) {
    handleCorrectButtonPress(buttonPressed);
  } else if (buttonPressed != -1) {
    resetGame();
  }
}

int findPressedButton() {
  for (int i = 0; i < 5; i++) {
    if (digitalRead(inputPins[i]) == LOW) {
      return inputPins[i];
    }
  }
  return -1;
}

void handleCorrectButtonPress(int buttonPressed) {
  Serial.println("Button pressed: " + String(buttonPressed));
  lastButtonPressed = buttonPressed;
  ledsActive[sequenceIndex] = true;
  digitalWrite(relayPins[sequenceIndex], HIGH);
  sequenceIndex++;
  
  if (sequenceIndex == sequenceLength) {
    Serial.println("Correct sequence matched!");
  }
}

void resetGame() {
  Serial.println("Resetting...");
  sequenceIndex = 0;
  lastButtonPressed = -1;
  for (int i = 0; i < 4; i++) {
    ledsActive[i] = false;
    digitalWrite(relayPins[i], LOW);
  }
  ledsOn = false;
  Serial.println("Game restarted from the beginning.");
}

void activateAllRelays() {
  for (int i = 0; i < 4; i++) {
    digitalWrite(relayPins[i], HIGH);
  }
  delay(1000);
  resetGame();
}
