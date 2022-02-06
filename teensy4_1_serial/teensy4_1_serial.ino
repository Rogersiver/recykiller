#include <Bounce.h>

Bounce b1 = Bounce( 3, 500); 
Bounce b2 = Bounce( 4, 500);
Bounce b3 = Bounce( 5, 500);
Bounce b4 = Bounce( 6, 500);

void setup() {
    Serial.begin(9600);
        pinMode(3, INPUT_PULLUP);
        pinMode(4, INPUT_PULLUP);
        pinMode(5, INPUT_PULLUP);
        pinMode(6, INPUT_PULLUP);
}

void loop() {
        b1.update();
        b2.update();
        b3.update();
        b4.update();
        if (b1.fallingEdge()) {
            Serial.println("Button 1");
        }
        if (b2.fallingEdge()) {
            Serial.println("Button 2");            
        }
}
