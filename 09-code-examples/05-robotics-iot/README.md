# Smart Irrigation Controller

The Arduino demonstration from `PROGRAMMING-FRAMEWORK.md` (Pathway 5).

## Hardware

- Arduino board
- Soil moisture sensor with analog output
- Suitable low-voltage pump (or an LED for the first test)
- Appropriate transistor or motor driver
- External power supply suitable for the pump
- Common ground where required

## Safety

- Start with a **simulated circuit** (Tinkercad Circuits) or an **LED demonstration** before using a pump.
- Do **not** connect a pump directly to an Arduino output pin — use a driver, a suitable power supply and protection components.
- Calibrate `moistureThreshold` for your sensor and soil; `500` is only a starting value.
- Use low-voltage educational equipment and teacher supervision.

## Try it

1. Open `smart-irrigation.ino` in Arduino IDE or Tinkercad Circuits.
2. Replace the pump with an LED for the first run.
3. Watch the Serial Monitor and change the threshold.
4. Record readings for later analysis (links to the Data Science pathway).
