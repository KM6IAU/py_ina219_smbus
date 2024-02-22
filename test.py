#!/usr/bin/python3


import time
from ina_219_smbus import ina219_i2c

ina219=ina219_i2c()

#ina219.set_cal(4096)
while(True):
	mV = False
	raw_value = ina219.get_shunt_voltage()
	shunt_voltage = round((raw_value>>3)*4*(0.001 if mV==False else 1),2)

	print(
		"bus V=", ina219.get_bus_voltage(mV=False),
		"sh V=", shunt_voltage,
		"A=", ina219.get_current(mA=False),
		"W=", ina219.get_power(mW=False)
	)
	time.sleep(1)
