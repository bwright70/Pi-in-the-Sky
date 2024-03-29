# 2023-01-04, Ian Novotne (inovotn04)
# Pi in the Sky
# Raspberry Pi Pico, Circuit Python v8

import board
import time
import digitalio
import adafruit_mpu6050
import busio
import adafruit_mpl3115a2
import microcontroller

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)  # Assigns SDA and SCL pins for sensor data

sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x60)  # Initialization of Altimeter
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)  # Initialization of MPU Accelerometer

led = digitalio.DigitalInOut(board.LED)
led.switch_to_output()  # Initialization of on-board LED

lucifer = 0

try:
    with open("/data.csv", "a") as fp:
        while True:
            lucifer = lucifer + 1
            x = mpu.acceleration[0]
            y = mpu.acceleration[1]
            z = mpu.acceleration[2]  # Pulls of all the mpu acceleration values
            anglex = mpu.gyro[0]
            angley = mpu.gyro[1]
            anglez = mpu.gyro[2]
            if lucifer == 665:
                fp.write(f"HAIL SATAN\n")
                fp.flush()
            print(
                f"x: {x} m/s^2  y: {y} m/s^2 z: {z} m/s^2 \n Altitude: {sensor.altitude}"
            ) # Data formatted and printed to console (also pulls altimeter altitude)

            fp.write(f"{time.monotonic()},{x},{y},{z},{sensor.altitude},{anglex},{angley},{anglez}\n") # Writes data to temperature.csv
            fp.flush()
            led.value = not led.value
            time.sleep(1)

except OSError as e:  # Typically when the filesystem isn't writeable...
    delay = 0.25  # ...blink the LED every half second.
    if e.args[0] == 28:  # If the file system is full...
        delay = 0.1  # ...blink the LED faster!
    while True:
        led.value = not led.value
        time.sleep(delay)
