from machine import Pin, I2C
from BMI160 import BMI160_I2C
from time import sleep_ms
from vibration_status import (
    device_found_info,
    device_not_found_error,
    wrong_posture_alert,
    posture_ok_info,
    beggining_loop_info
)

QUICK_VIBRATION = 500
LONG_BREAK = 2000

threshold = 300
interval = 2 # in secconds

# device initialization
pin2 = Pin(2, Pin.OUT)

# Initialize I2C
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=100000)

# Scan for devices
devices = i2c.scan()

if devices:
    device_found_info(pin2, QUICK_VIBRATION, LONG_BREAK)
else:
    device_not_found_error(pin2, QUICK_VIBRATION, LONG_BREAK)

bmi160 = BMI160_I2C(i2c)

startX = 0
startY = 0
startZ = 0

refreshspersecond = 20

for _ in range(interval*1000/refreshspersecond):
    startX += bmi160.getAcceleration()[0]
    startY += bmi160.getAcceleration()[1]
    startZ += bmi160.getAcceleration()[2]
    sleep_ms(int(1000/refreshspersecond))
    
startX = startX / (5*1000/refreshspersecond)
startY = startY / (5*1000/refreshspersecond)
startZ = startZ / (5*1000/refreshspersecond)

beggining_loop_info(pin2, QUICK_VIBRATION, LONG_BREAK)

print(f"sX:{startX}|sY:{startY}|sZ:{startZ}")

while True:
    actualX = 0
    actualY = 0
    actualZ = 0

    for _ in range(interval*1000/refreshspersecond):
        actualX += bmi160.getAcceleration()[0]
        actualY += bmi160.getAcceleration()[1]
        actualZ += bmi160.getAcceleration()[2]
        sleep_ms(int(1000/refreshspersecond))

    actualX = actualX / (5*1000/refreshspersecond)
    actualY = actualY / (5*1000/refreshspersecond)
    actualZ = actualZ / (5*1000/refreshspersecond)

    print(f"aX:{actualX}|aY:{actualY}|aZ:{actualZ}")

    if actualX + threshold > startX > actualX - threshold or \
       actualY + threshold > startY > actualY - threshold or \
       actualZ + threshold > startZ > actualZ - threshold:
        posture_ok_info()
    else:
        wrong_posture_alert(pin2, QUICK_VIBRATION, LONG_BREAK)

