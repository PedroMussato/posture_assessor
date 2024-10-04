from time import sleep_ms


def device_found_info(pin, QUICK_VIBRATION, LONG_BREAK):
    print("INFO : DEVICE FOUND")
    pin.value(1)
    sleep_ms(QUICK_VIBRATION)
    pin.value(0)


def device_not_found_error(pin, QUICK_VIBRATION, LONG_BREAK):
    print("ERROR : DEVICE NOT FOUND")
    while True:
        pin.value(1)
        sleep_ms(QUICK_VIBRATION)
        pin.value(0)
        
        pin.value(1)
        sleep_ms(QUICK_VIBRATION)
        pin.value(0)
        
        sleep_ms(LONG_BREAK)

def wrong_posture_alert(pin, QUICK_VIBRATION, LONG_BREAK):
    print("INFO : WRONG POSTURE ALERT")
    pin.value(1)
    sleep_ms(QUICK_VIBRATION*3)
    pin.value(0)

def posture_ok_info():
    print("INFO : POSTURE OK")
    
def beggining_loop_info(pin, QUICK_VIBRATION, LONG_BREAK):
    print("INFO : BEGGINING LOOP")
    pin.value(1)
    sleep_ms(QUICK_VIBRATION)
    pin.value(0)
