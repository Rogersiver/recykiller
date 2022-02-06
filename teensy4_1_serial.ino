#include <Bounce.h>

Bounce b1 = Bounce( 1, 3000);
Bounce b2 = Bounce( 2, 3000);
Bounce b3 = Bounce( 3, 3000);
Bounce b4 = Bounce( 4, 3000);
Bounce b5 = Bounce( 5, 3000);
Bounce b6 = Bounce( 6, 3000);
Bounce b7 = Bounce( 7, 3000);
Bounce b8 = Bounce( 8, 3000);
Bounce b9 = Bounce( 9, 3000);
Bounce b10 = Bounce( 10, 3000);
Bounce b11 = Bounce( 11, 3000);
Bounce b12 = Bounce( 12, 3000);
Bounce b13 = Bounce( 13, 3000);
Bounce b14 = Bounce( 14, 3000);
Bounce b15 = Bounce( 15, 3000);
Bounce b16 = Bounce( 16, 3000);

void setup() {
    Serial.begin(512000);
for(int i=1; i<=16; i++) {
pinMode(i, INPUT_PULLUP);
}
}

void loop() {
        b1.update();
        b2.update();
        b3.update();
        b4.update();
        b5.update();
        b6.update();
        b7.update();
        b8.update();
        b9.update();
        b10.update();
        b11.update();
        b12.update();
        b13.update();
        b14.update();
        b15.update();
        b16.update();

        if (b1.fallingEdge()) {
            Serial.println("01");
        }
        if (b2.fallingEdge()) {
            Serial.println("02");
        }
        if (b3.fallingEdge()) {
            Serial.println("03");
        }
        if (b4.fallingEdge()) {
            Serial.println("04");
        }
        if (b5.fallingEdge()) {
            Serial.println("05");
        }
        if (b6.fallingEdge()) {
            Serial.println("06");
        }
        if (b7.fallingEdge()) {
            Serial.println("07");
        }
        if (b8.fallingEdge()) {
            Serial.println("08");
        }
        if (b9.fallingEdge()) {
            Serial.println("09");
        }
        if (b10.fallingEdge()) {
            Serial.println("10");
        }
        if (b11.fallingEdge()) {
            Serial.println("11");
        }
        if (b12.fallingEdge()) {
            Serial.println("12");
        }
        if (b13.fallingEdge()) {
            Serial.println("13");
        }
        if (b14.fallingEdge()) {
            Serial.println("14");
        }
        if (b15.fallingEdge()) {
            Serial.println("15");
        }
        if (b16.fallingEdge()) {
            Serial.println("16");
        }

}
