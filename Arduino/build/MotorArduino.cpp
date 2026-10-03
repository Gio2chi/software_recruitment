#include "fakeArduino.hpp"
#include "fakeArduino.hpp"
#define SAMPLE_RATE 100 

#define JOYSTICK_PIN A2

#define MOTOR_INSTRUCTION_ID 0x1E
#define MOTOR_LOW 818
#define MOTOR_HIGH 511

void setup(){
    // pinMode(JOYSTICK_PIN, INPUT);
    Serial.begin(19200);
}

unsigned long last_sample = 0;
void loop(){
    unsigned long now = millis();
    if (now - last_sample >= SAMPLE_RATE){
        last_sample = now;
        uint16_t cmd_read = analogRead(JOYSTICK_PIN); // a read of 0-1023
        // printf("Read: %d\n", cmd_read);
        uint16_t cmd_adjusted = map(cmd_read, 0, 1023, MOTOR_LOW, MOTOR_HIGH);
        // printf("Adjusted: %d\n", cmd_adjusted);
        Serial.write(MOTOR_INSTRUCTION_ID);
        Serial.write((uint8_t*)&cmd_adjusted, sizeof(uint16_t));
    }
}