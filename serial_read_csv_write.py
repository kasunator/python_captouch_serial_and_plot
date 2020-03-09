"""this file implements a function that will read the data
given by the serial port just like the serial_program.py but this time it writes to
csv file, the idea is to write another program which will read the .csv file for ploting

the data is formatted in the following way
KASUN:PROX STAT READING:0
KASUN:[0]=14,[ID]=1,[CP]=c,[DIFF]=0,[BASELINE]=b7ad,[RAW]b7ad,[AVG]=b7c9,[12]=14

"KASUN:PROX STAT READING:%d\n"
"KASUN:PROX STAT READING ORIGINAL:%d\n";
"""

import serial
import time
import csv
from datetime import datetime
#ser = serial.Serial()
#ser_bytes = ser.readline()
#print(ser_bytes)
#KASUN:PROX STAT READING:0
#KASUN:PROX STAT READING:1
#KASUN:[DIFF]=39,[BASELINE]=ba8a,[RAW]=bab0,[AVG]=ba96


def  extract_prox_stat_result(rx_string):
	result = 0
	prox_stat_index = rx_string.find("PROX STAT READING:")
	prox_stat_result = rx_string[prox_stat_index + len("PROX STAT READING:"):]
	if prox_stat_result[0] == '1' :
		result = 1
	elif prox_stat_result[0] == '2' :
		result = 2
	elif prox_stat_result[0] == '3':
	 	result = 3
	elif prox_stat_result[0] == '0':
		result =0
	else :
		print("result unknown")
	return result

def  extract_prox_stat_result_original(rx_string):
	result = 0
	prox_stat_index = rx_string.find("PROX STAT READING ORIGINAL:")
	prox_stat_result = rx_string[prox_stat_index + len("PROX STAT READING ORIGINAL:"):]
	if prox_stat_result[0] == '1' :
		result = 1
	elif prox_stat_result[0] == '2' :
		result = 2
	elif prox_stat_result[0] == '3':
	 	result = 3
	elif prox_stat_result[0] == '0':
		result =0
	else :
		print("result unknown")
	return result

def check_if_prox_stat(rx_string):
	prox_stat_index = rx_string.find("PROX STAT READING:")
	if prox_stat_index != -1 :
		return True
	else :
		return False
def check_if_prox_stat_original(rx_string):
	prox_stat_index = rx_string.find("PROX STAT READING ORIGINAL:")
	if prox_stat_index != -1 :
		return True
	else :
		return False

def extract_DIFF_count(rx_string) :
	_DIFF_index = rx_string.find("[DIFF]=")
	if _DIFF_index != -1 :
		remainder_from_DIFF_string = rx_string[_DIFF_index + len("[DIFF]="):]
		comma_index=remainder_from_DIFF_string.find(",")
		if comma_index != -1 :
			print("[DIFF]= index ="+ str(_DIFF_index) +"\n")
			print("comma index ="+ str(comma_index) +"\n")
			data_string = remainder_from_DIFF_string[:comma_index]
			print("[DIFF] data string" + data_string)
			print("[DIFF] integer value = "+ str(int(data_string,16))+ "\n")
		else :
			print("didnt find ',' delemeter")
	else :
		print("didn't find [DIFF]")
"""
this is very simmilar to extract_DIFF_count(rx_string)
except more general so we can pass the string patern of the data identifier
as a pattern,as an example in case of DIFF data we can pass "[DIFF]=",
This will extract the data in integer form between "[DIFF]=" and the first following
','after that  and return it"""
def extract_data_value(data_tag, rx_string) :
	tag_index = rx_string.find(data_tag)
	if tag_index != -1 :
		remainder_from_data_tag_string = rx_string[tag_index + len(data_tag):]
		comma_index=remainder_from_data_tag_string.find(",")
		if comma_index != -1 :
			#print(data_tag + "index ="+ str(tag_index) +"\n")
			#print("comma index ="+ str(comma_index) +"\n")
			data_string = remainder_from_data_tag_string[:comma_index]
			#print(data_tag + "data string in hex" + data_string)
			#print(data_tag + "integer value = "+ str(int(data_string,16))+ "\n")
			return int(data_string,16)
		else :
			print("didnt find ',' delemeter")
			return -1
	else :
		print("didn't find" + data_tag)
		return -1

""" the main function starts here"""
now = datetime.now().strftime("%H:%M:%S")
diff = 0
baseline =0
raw = 0
avg = 0
result = 0
result_original =0

port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=3.0)

fieldnames = ["time","diff","baseline","raw","avg","result","result_original"]

with open('python_captouch_data.csv','w') as csv_file :
    csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
    csv_writer.writeheader()

while True:

	rx_string  = port.readline().decode('utf-8')
	kasun_tag_index = rx_string.find("KASUN:")
	if kasun_tag_index != -1 :
		rx_string_data = rx_string[kasun_tag_index + len("KASUN:"):]
		#print("Rx string data " + rx_string_data)
		if check_if_prox_stat(rx_string_data) == False and check_if_prox_stat_original(rx_string_data) == False :
			#print("this is not prox stat")
			#extract_DIFF_count(rx_string_data)
			diff = extract_data_value(data_tag = "[DIFF]=",rx_string = rx_string_data)
			#extract [BASELINE]
			baseline = extract_data_value(data_tag = "[BASELINE]=",rx_string = rx_string_data)
			#extract [RAW]
			raw = extract_data_value(data_tag = "[RAW]=",rx_string = rx_string_data)
			#extract [AVG]
			avg = extract_data_value(data_tag = "[AVG]=",rx_string = rx_string_data)
			#print("diff =" + str(diff) )
			#ok now lets write this data to our file
			now = datetime.now().strftime("%H:%M:%S")
			#row = [now, diff]
			"""
			with open('python_captouch_data.csv', 'a') as f:
				#writer = csv.writer(f)
				writer = csv.DictWriter(f, fieldnames = fieldnames)
				info = {
					"time":now,
					"diff":diff,
					"baseline":baseline,
					"raw":raw,
					"avg":avg
				}
				writer.writerow(info)
				#writer.writerow(row)
			"""
		else :
			if check_if_prox_stat_original(rx_string_data) == True :
				result_original = extract_prox_stat_result_original(rx_string)
				print("this is prox stat original"+ str(result_original))
			elif check_if_prox_stat(rx_string_data) == True:
				result = extract_prox_stat_result(rx_string_data)
				print("this is prox stat"+ str(result))
			else:
				print("decode error")

			with open('python_captouch_data.csv', 'a') as f:
				#writer = csv.writer(f)
				writer = csv.DictWriter(f, fieldnames = fieldnames)
				info = {
					"time":now,
					"diff":diff,
					"baseline":baseline,
					"raw":raw,
					"avg":avg,
					"result":result,
					"result_original":result_original,
				}
				writer.writerow(info)

		#print("kasun index found")
	else :
		print("kasun index not found")
