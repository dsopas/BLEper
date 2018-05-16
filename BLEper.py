#
# BLEper.py by @dsopas
# Usage: sudo python BLEper.py 'bd_addr'
#
import pygatt, time, sys, subprocess
from time import sleep

ADDRESS_TYPE = pygatt.BLEAddressType.random
adapter = pygatt.GATTToolBackend()

if len(sys.argv) < 2:
 	print "- Hey! Pass the bd_addr to track it"
	print "- Usage: sudo python BLEper.py 'bd_addr'"
	sys.exit(1)
else:
    bd_addr = sys.argv[1]

adapter.start()
print "- BLEper started..."
print "- Start scanning..."

def beepar():
	# You can change the wav file to your needs
	subprocess.check_output(['aplay', '/usr/share/sounds/alsa/Front_Center.wav', '-q'])
	time.sleep(1)
try:
	while True:
		devices = adapter.scan(run_as_root=True, timeout=3)
		for device in devices:
			if device['address'] == bd_addr:
				print "- Found it..."
				print "- " + device['address'] + " [" + device['name'] + "]"
				beepar()
		time.sleep(3)
except KeyboardInterrupt:
    print "Stop!"
