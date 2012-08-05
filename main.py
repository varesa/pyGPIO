## Imports

from os.path import exists, join

from enums import *

## Sets of allowed values

GPIO_PINS = (GPIO_0, GPIO_1, GPIO_4, GPIO_7, GPIO_8, GPIO_9, GPIO_10, GPIO_11, GPIO_14, GPIO_15, GPIO_17, GPIO_18, GPIO_21, GPIO_22, GPIO_23, GPIO_24, GPIO_25)
DIRECTIONS = (IN, OUT)

## Constants

GPIO_PATH = "/sys/class/gpio"

## Functions

def isExported(port):
    if port not in GPIO_PINS:
	raise Exception('Unknown port')
    if exists(join(GPIO_PATH, "gpio" + str(port))):
	return True
    return False

def getDirection(port):
    if port not in GPIO_PINS:
	raise Exception('Unknown port')
    if not isExported(port):
	raise Exception('The port has not been exported')

    with open(join(GPIO_PATH, "gpio" + str(port), "direction")) as dir_file:
	direction = dir_file.read()
	return direction.strip()

def setDirection(port, direction):
    if port not in GPIO_PINS:
	raise Exception('Unknown port')
    if direction not in DIRECTIONS:
	raise Exception('Invalid direction')
    if not isExported(port):
	raise Exception('The port has not been exported')

    with open(join(GPIO_PATH, "gpio" + str(port), "direction"), "w") as dir_file:
	dir_file.write(direction)
