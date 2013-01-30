import serial

SERIAL_PATH = '/dev/ttyAMA0'
SERIAL_SPEED = 9600

def main():
	global serial_connection, SERIAL_PATH
	try:
		serial_connection = serial.Serial(SERIAL_PATH, SERIAL_SPEED)
		serial_connection.write(chr(13).__str__())
	except:
		print "Problem connecting to arduino"
		exit()
	default = ''
	while default.__len__() < 1:
		default = raw_input('Default: ')

	while True:
		indata = raw_input('Send? ')
		if indata.__len__() < 1:
			send(default)
		else:
			send(indata)
		
def send(data):
	serial_connection.write(chr(int(data) + 20).__str__())
	print "Wrote", data, "(", chr(int(data) + 20).__str__(), ") over serial"

if __name__ == '__main__':
	main()
