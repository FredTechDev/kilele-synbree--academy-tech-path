// Smart Irrigation Controller — Kilele TechPath, Pathway 5 (Robotics & IoT)
// Educational demonstration. Start with a simulated circuit or LED.
// Do NOT connect a pump directly to an Arduino output pin.

const int soilSensor = A0;
const int pumpPin = 8;

const int moistureThreshold = 500;

void setup() {

    Serial.begin(9600);

    pinMode(pumpPin, OUTPUT);

    digitalWrite(pumpPin, LOW);
}

void loop() {

    int moistureValue = analogRead(soilSensor);

    Serial.print("Soil Moisture Reading: ");
    Serial.println(moistureValue);

    if (moistureValue > moistureThreshold) {

        digitalWrite(pumpPin, HIGH);

        Serial.println("Soil is dry. Irrigation activated.");

    } else {

        digitalWrite(pumpPin, LOW);

        Serial.println("Soil moisture is sufficient.");
    }

    delay(2000);
}
