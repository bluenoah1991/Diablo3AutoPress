# Diablo3AutoPress

![photo](https://github.com/codemeow5/Diablo3AutoPress/raw/master/photo.jpg)

### reference links

- https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid/
- https://www.rmedgar.com/blog/using-rpi-zero-as-keyboard-setup-and-device-definition
- https://www.rmedgar.com/blog/using-rpi-zero-as-keyboard-report-descriptor

### install guide

copy the `vkb_usb` file to /usr/bin

insert the following line into the `/etc/rc.local`

	/usr/bin/vkb_usb

connect `pi zero w` to computer and reboot system

execute `press.py` script

	sudo python press.py

or use `press_auto.py` that supports hardware buttons

	sudo python press_auto.py

