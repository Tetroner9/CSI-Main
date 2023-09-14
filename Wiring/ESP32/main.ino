#include <Arduino.h>

const int inputPins[] = {12, 13, 14, 27, 26};
const int relayPins[] = {19, 21, 22, 23};

// int sequence[] = {12, 13, 14, 27}; // Sequence 1 (Yellow, Blue, Orange, Pink)
// int buttonToLedMap[] = {19, 21, 22, 23}; // Corresponding LEDs for each button

// int sequence[] = {14, 12, 27, 13};  
// int buttonToLedMap[] = {22, 19, 23, 21};

// int sequence[] = {27, 13, 14, 12};  
// int buttonToLedMap[] = {23, 21, 22, 19};

int sequence[] = {12, 27, 13, 14};  
int buttonToLedMap[] = {19, 23, 21, 22};

// int sequence[] = {14, 27, 13, 12};  
// int buttonToLedMap[] = {22, 23, 21, 19};  

// int sequence[] = {12, 14, 27, 13};   
// int buttonToLedMap[] = {19, 22, 23, 21};

const int sequenceLength = 4;

bool ledsActive[] = {false, false, false, false};

int sequenceIndex = 0;
bool ledsOn = false;
int lastButtonPressed = -1;
unsigned long sequenceTimeout = 0;
const unsigned long timeoutDuration = 5000; // 5 seconds timeout

const unsigned long debounceDelay = 500; // 500 milliseconds debounce delay

unsigned long lastButtonPressTime = 0; // Store the timestamp of the last button press

void setup() {
  for (int i = 0; i < 4; i++) {
    pinMode(inputPins[i], INPUT_PULLUP);
    pinMode(relayPins[i], OUTPUT);
    digitalWrite(relayPins[i], HIGH);
  }
  pinMode(inputPins[4], INPUT_PULLUP);
   randomizeSequence();
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(inputPins[4]) == LOW) {
    resetGame();
  } else {
    if (sequenceIndex < sequenceLength) {
      checkSequenceWithDebounce();
    }

    if (sequenceIndex == sequenceLength && !ledsOn) {
      blinkLeds();
      resetGame();
      activateAllRelays();
      ledsOn = true;
    }

    // Check for timeout
    if (sequenceIndex > 0 && millis() - sequenceTimeout >= timeoutDuration) {
      resetGame();
      Serial.println("Timeout! You took too long to press the next button.");
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
  digitalWrite(buttonToLedMap[sequenceIndex], LOW);  // Activate the corresponding LED
  sequenceIndex++;

  if (sequenceIndex == sequenceLength) {
    Serial.println("Correct sequence matched!");
    randomizeSequence();
  } else {
    // Reset the timeout timer for the next button press
    sequenceTimeout = millis();
  }
}

void resetGame() {
  Serial.println("Resetting...");
  sequenceIndex = 0;
  lastButtonPressed = -1;
  for (int i = 0; i < 4; i++) {
    ledsActive[i] = false;
    digitalWrite(relayPins[i], HIGH);
  }
  ledsOn = false;
  sequenceTimeout = 0; // Reset the timeout timer
  Serial.println("Game restarted from the beginning.");
}

void activateAllRelays() {
  for (int i = 0; i < 4; i++) {
    digitalWrite(relayPins[i], LOW);
  }
  delay(250);
  resetGame();
}

void displaySequence() {
  for (int i = 0; i < sequenceLength; i++) {
    digitalWrite(buttonToLedMap[i], LOW);  // Turn on the corresponding LED
    delay(250); // Delay to keep the LED on for a short time
    digitalWrite(buttonToLedMap[i], HIGH); // Turn off the LED
    delay(250); // Delay to keep the LED off for a short time
    
  }
}

void blinkLeds() {
  activateAllRelays();
  resetGame(); // Reset the game state before displaying the sequence


  unsigned long startTime = millis(); // Record the start time
  unsigned long duration = 10000; // 10 seconds duration

  // Define patterns for each LED
  int patterns[][2] = {
    {HIGH, 250},  // LED on for 250ms
    {LOW, 100},   // LED off for 100ms
    {HIGH, 100},  // LED on for 100ms
    {LOW, 250},   // LED off for 250ms
  };

  while (millis() - startTime < duration) {
    for (int i = 0; i < 2; i++) { // Repeat the sequence twice
      for (int j = 0; j < 4; j++) {
        for (int k = 0; k < sequenceLength; k++) {
          digitalWrite(buttonToLedMap[k], patterns[j][0]);  // Turn on/off the corresponding LED
          delay(patterns[j][1]); // Delay based on the pattern
        }
      }
    }
  }
  resetGame();
  delay(250);
}

void checkSequenceWithDebounce() {
  if (sequenceIndex < 0 || sequenceIndex >= sequenceLength) {
    return;
  }

  int buttonPressed = findPressedButton();

  if (buttonPressed != -1) {
    // Check for debounce delay
    if (millis() - lastButtonPressTime >= debounceDelay) {
      lastButtonPressTime = millis(); // Update the last button press time
      if (buttonPressed == sequence[sequenceIndex]) {
        handleCorrectButtonPress(buttonPressed);
      } else {
        resetGame();
      }
    }
  }
}

void randomizeSequence() {
  int currentIndex, randomIndex, temp;
  
  // Initialize random seed
  randomSeed(analogRead(0));

  // Start from the end of the array and swap each element with a random element before it
  for (currentIndex = sequenceLength - 1; currentIndex > 0; currentIndex--) {
    randomIndex = random(0, currentIndex + 1); // Generate a random index from 0 to currentIndex

    // Swap sequence[currentIndex] and sequence[randomIndex]
    temp = sequence[currentIndex];
    sequence[currentIndex] = sequence[randomIndex];
    sequence[randomIndex] = temp;

    // Also swap buttonToLedMap[currentIndex] and buttonToLedMap[randomIndex]
    temp = buttonToLedMap[currentIndex];
    buttonToLedMap[currentIndex] = buttonToLedMap[randomIndex];
    buttonToLedMap[randomIndex] = temp;
  }
}