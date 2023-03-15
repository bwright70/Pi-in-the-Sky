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
import pwmio

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)  # Assigns SDA and SCL pins for sensor data

sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x60)  # Initialization of Altimeter
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)  # Initialization of MPU Accelerometer

led = digitalio.DigitalInOut(board.LED)
led.switch_to_output()  # Initiliazation of on-board LED

MOTOR_1 = board.GP11
MOTOR_2 = board.GP21
MOTOR_3 = board.GP20
MOTOR_4 = board.GP10    #Sets motor pins wowza
rightmotor_pwm = pwmio.PWMOut(MOTOR_1, frequency=1000)
leftmotor_pwm = pwmio.PWMOut(MOTOR_2, frequency=1000)
upmotor_pwm = pwmio.PWMOut(MOTOR_3, frequency=1000)
downmotor_pwm = pwmio.PWMOut(MOTOR_4, frequency=1000)   #Initializes motors and sets frequency

try:
    with open("/temperature.csv", "a") as fp:
        while True:
            #get bluetooth input
            if #bluetoothinput = right:
                leftmotor_pwm.duty_cycle = 65535 // 2  # Cycles the pin with 50% duty cycle (half of 2 ** 16)
                rightmotor_pwm.duty_cycle = 0  # Turns right motor off
            if #bluetoothinput = left
                rightmotor_pwm.duty_cycle = 65535 // 2  # Cycles the pin with 50% duty cycle (half of 2 ** 16)
                leftmotor_pwm.duty_cycle = 0  #Turns left motor off
            if #bluetoothinput = up
                upmotor_pwm.duty_cycle = 65535 // 2  # Cycles the pin with 50% duty cycle (half of 2 ** 16)
                downmotor_pwm.duty_cycle = 0 # Turns down motor off
            if #bluetoothinpt = down
                downmotor_pwm.duty_cycle = 65535 // 2  # Cycles the pin with 50% duty cycle (half of 2 ** 16)
                upmotor_pwm.duty_cycle = 0 #Turns up motor off
            else:
                rightmotor_pwm.duty_cycle = 0
                leftmotor_pwm.duty_cycle = 0
                downmotor_pwm.duty_cycle = 0
                upmotor_pwm.duty_cycle = 0  #Turns motors off if no input


            x = mpu.acceleration[0]
            y = mpu.acceleration[1]
            z = mpu.acceleration[2]  # Pulls of all the mpu acceleration values

            print(
                f"x: {x} m/s^2  y: {y} m/s^2 z: {z} m/s^2 \n Altitude: {sensor.altitude}"
            ) # Data formatted and printed to console (also pulls altimeter altitude)

            fp.write(f"{x},{y},{z},{sensor.altitude}\n") # Writes data to temperature.csv
            fp.flush()

except OSError as e:  # Typically when the filesystem isn't writeable...
    delay = 0.25  # ...blink the LED every quarter second.
    if e.args[0] == 28:  # If the file system is full...
        delay = 0.1  # ...blink the LED faster!
    while True:
        led.value = not led.value
        time.sleep(delay)
