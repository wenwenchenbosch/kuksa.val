#!/usr/bin/python3

########################################################################
# Copyright (c) 2020 Robert Bosch GmbH
#
# This program and the accompanying materials are made
# available under the terms of the Eclipse Public License 2.0
# which is available at https://www.eclipse.org/legal/epl-2.0/
#
# SPDX-License-Identifier: EPL-2.0
########################################################################




import argparse
import sys
import time

import obdconnector as obdC
import obd2vssmapper
import yaml

cfg={}
cfg['TIMEOUT']=60



def getConfig():
	global cfg
	parser = argparse.ArgumentParser()
	parser.add_argument("-t", "--timeout",  default=1, help="Timeout between read cylces", type=int)
	parser.add_argument("-b", "--baudrate", default=2000000, help="Baudrate to ELM", type=int)
	parser.add_argument("-d", "--device",   default="/dev/ttyAMA0", help="Serial port for ELM connection", type=str)
	parser.add_argument("--mapping",   default="mapping.yml", help="VSS mapping", type=str)
	
	args=parser.parse_args()
	cfg['TIMEOUT']=args.timeout
	cfg['baudrate']=args.baudrate
	cfg['device']=args.device
	cfg['mapping']=args.mapping

    



            


def publishData():
	print("Publish data")



print("kuksa.val OBD example feeder")
getConfig()
print("Configuration")
print("Device       : {}".format(cfg['device']))
print("Baudrate     : {} baud".format(cfg['baudrate']))
print("Timeout      : {} s".format(cfg['TIMEOUT']))
print("Mapping file : {}".format(cfg['mapping']))


connection = obdC.openOBD(cfg['device'],cfg['baudrate'])

mapping=obd2vssmapper.mapper("mapping.yml")

while True:
	obdC.collectData(mapping,connection)
	publishData()
#	response=connection.query(cmd)
#	if not response.is_null():
#		print("Speed is {}, or {} ".format(response.value,response.value.to("mph")))
#	else:
#		print("No data from car. Are you connected to OBD? Is your STN set to 2Mbit baudrate?")
#	print("Have you started porting VRTE to me?\n")
	time.sleep(cfg['TIMEOUT'])
