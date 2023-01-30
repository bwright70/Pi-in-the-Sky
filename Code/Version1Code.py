import board
import time
import digitalio
import adafruit_mpu6050
import busio
import adafruit_mpl3115a2
import microcontroller

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin) 

sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x60) #Altimeter init
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68) #mpu init

led = digitalio.DigitalInOut(board.LED)
led.switch_to_output()

try:
    with open("/temperature.csv", "a") as fp:      
        while True:
            x = mpu.acceleration[0]
            y = mpu.acceleration[1]
            z = mpu.acceleration[2] #Pulls all the mpu acceleration values

            print(f"x: {x} m/s^2  y: {y} m/s^2 z: {z} m/s^2 \n Altitude: {sensor.altitude}")

#            fp.write(f"x: {x} m/s^2  y: {y} m/s^2 z: {z} m/s^2 \n Altitude: {sensor.altitude}")
            fp.write(f"{x},{y},{z},{sensor.altitude}\n")
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
        #aaaa