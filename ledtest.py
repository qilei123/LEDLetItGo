#!/usr/bin/python

import RPi.GPIO as GPIO, time

# Configurable values
dev       = "/dev/spidev0.0"

# Open SPI device, load image in RGB format and get dimensions:
spidev    = file(dev, "wb")

# Calculate gamma correction table.  This includes
# WS2801-specific conversion.
gamma = bytearray(256)
for i in range(256):
	gamma[i] = int(pow(float(i) / 255.0, 2.5) * 255.0 + 0.5)

test_set = bytearray(25 * 3);
for y in range(255):
	for x in range(25):
		test_set[x*3    ] = gamma[y]
        	test_set[x*3 + 1] = gamma[00]
        	test_set[x*3 + 2] = gamma[255-y]
	spidev.write(test_set)
	spidev.flush()
	time.sleep(0.06)
print "Done!"
