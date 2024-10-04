# parts needed
 Raspberry pi pico (RP2040 is good enough)
 ![61qfc9KJPdL _AC_UF1000,1000_QL80_](https://github.com/user-attachments/assets/4df6d73c-8909-4a1d-83ea-0df640d762ad)
 Bosch BMI160
 ![710CMl3F9KL _AC_UF1000,1000_QL80_](https://github.com/user-attachments/assets/e3d083af-5738-42f6-afcc-a70555e08428)

# Mounting
  Solder the 3v3 of the raspberry pi on the 3v3 of the bmi160
  Solder the GND of the raspberry pi on the GND of the bmi160
  Solder the PIN0 of the raspberry pi on the SDA of the bmi160
  Solder the PIN1 of the raspberry pi on the SCL of the bmi160
  Upload the code that is on this repo and that is done.

# Battery
  Must to be a 3v7 battery, cr2032 works but not for long.
  You can also use a TP4056 module to charge the battery and connect to the 5v and GND of the RP2040 to have only one USBC
  ![5121ZtfM-hL _AC_UF1000,1000_QL80_](https://github.com/user-attachments/assets/c6f69801-2a9d-43f1-a292-da78778775a4)

# More to come
  3D printed case to fit everything and use as a botton that is not this ugly.
