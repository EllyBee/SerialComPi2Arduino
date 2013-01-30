# Notes for setting up serial communication between pi and arduino:

Comment out this line in Pi's /etc/inittab

# 2:23:respawn:/sbin/getty -L ttyAMA0 115200 vt100

If you don’t want the Pi sending stuff over the serial line when it boots, you can also 
remove the statements 

console=ttyAMA0,115200 and kgdboc=ttyAMA0,115200 from /boot/cmdline.txt. 

You’ll need to reboot the Pi in order for the changes to take effect.

Wiring:

Pi RX > Arduino's TX
Pi TX > Arduino's RX

Pi GND > Arduino GND

(You can also link up Pi 5V > Arduino Vin if you want to power Arduino too)

To run python code on Pi you need to install pyserial. If pip doesn't work try 
easy_install.

Reference:
http://codeandlife.com/2012/07/29/arduino-and-raspberry-pi-serial-communication/
