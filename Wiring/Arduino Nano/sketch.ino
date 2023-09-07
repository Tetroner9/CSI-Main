#include <Arduino.h>

const int inputPins[] = {A3, A2, A1, A0, A4};
const int relayPins[] = {2, 3, 4, 5};
const int sequence[] = {A3, A2, A1, A0};
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
  Serial.print("Resetting...");
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
