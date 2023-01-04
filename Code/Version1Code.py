import board
import time
import digitalio
import adafruit_mpu6050
import busio

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin) 

mpu = adafruit_mpu6050.MPU6050(i2c) #mpu init
sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x60) #Altimeter init
       
while True:
    x = mpu.acceleration[0]
    y = mpu.acceleration[1]
    z = mpu.acceleration[2] #Pulls all the mpu acceleration values

    print(f"x: {x} m/s^2  y: {y} m/s^2 z: {z} m/s^2 \n Altitude: {sensor.altitude}")

    time.sleep(0.1)