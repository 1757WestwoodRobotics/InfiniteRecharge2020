
#include <ArduinoJson.h>  // Make sure you use ArduinoJson 6 Libs.
#include <Joystick.h>

// Various Joy Stick Buttons for the Driver station and their Ardunio Pin outs
#define MIN_RANGE -512
#define MAX_RANGE  512
#define DS_BUTTON_COUNT 11   // We have 6 button, 5 toggle switches on the Driver Station

// Create Joystick
Joystick_ Joystick(JOYSTICK_DEFAULT_REPORT_ID,
                   JOYSTICK_TYPE_JOYSTICK,
                   DS_BUTTON_COUNT,
                   0,  // No HAT switch
                   true,  // X- Axis only
                   false,
                   false,
                   false,
                   false,
                   false,
                   false,
                   false,
                   false,
                   false,
                   false);

// Arduino Pins the buttons are connected to
const int buttons[DS_BUTTON_COUNT] = {0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11};

// Global Variables hold object distance as seen by the ultrasonic sensor, led commands etc.
boolean debug = false;
boolean touched = true;
const bool autoSendMode = true;



void setup() {

  // set up console baud rate
  Serial.begin(115200);
  Serial.print("Initilizing....\n");
  // Built in LED pin 13 as output
  pinMode (LED_BUILTIN, OUTPUT);

  // Configure JS buttons


  //  Configure All buttons. Since we run out of Digital Pins we will use 2 Analog pins to serve as digital pins.
  for (int pin = 0; pin < 12; pin++)
    pinMode(pin, OUTPUT);

  // Joystick initialization
  // Set Range Values
  Joystick.setXAxisRange(MIN_RANGE, MAX_RANGE);
  Joystick.begin(autoSendMode);

  Serial.print("Initilization complete....\n");
}


void loop() {

  // Process Joystick
  processButtons();

  // Process any data over Serial Port.
  int how_many = 0;

  // Read  Serial PORT to see if you received a command
  if (how_many = Serial.available()) {
    if (debug) {
      Serial.print("Proccesing - ");
      Serial.print(how_many);
      Serial.println();
      Serial.print("Before JSON Parse...");
      Serial.print(millis());
      Serial.println();
    }
    DynamicJsonDocument read_doc(512);
    DeserializationError error =  deserializeJson(read_doc, Serial);

    if (debug) {
      Serial.print("After JSON Parse...");
      Serial.print(millis());
      Serial.println();
    }
    // Only if JSON Parse succeds do something or ignore the command
    if (!error) {
      const char *sensor = read_doc["sensor"];

    }
  }
}


// Sends JSON output to serial port: For testing only
void writeSerial(DynamicJsonDocument root) {
  serializeJson(root, Serial);
  Serial.println(); // Always send a CR at the end so reciever does not block.
  Serial.flush(); // Empty the buffer..
}


// Joystick Functions


void processButtons()
{
  boolean pressed = false;

  for (int i = 0; i < DS_BUTTON_COUNT; i++) {
    pressed = digitalRead(buttons[i]);
    // We are processing digial I/O pins
    if (debug) {
      Serial.print("Button [");
      Serial.print(i);
      Serial.print("] - ");
      Serial.print(pressed);
      Serial.println();
    }
    if (pressed) {
      Joystick.pressButton(i);
    }
    else {
      Joystick.releaseButton(i);
    }
  }
}
