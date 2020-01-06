import serial
#ser = serial.Serial()
#ser_bytes = ser.readline()
#print(ser_bytes)
#KASUN:PROX STAT READING:0
#KASUN:PROX STAT READING:1
#KASUN:[DIFF]=39,[BASELINE]=ba8a,[RAW]bab0,[AVG]=ba96
import serial

port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=3.0)

while True:

	#rcv = port.readline()
	rcv  = port.readline().decode('utf-8')
	index = rcv.find("KASUN:")
	if index != -1 :
		#print("KASUN found in;"+ rcv)
		rcv2 = rcv[index + len("KASUN:"):]
		#print("rcv2:" + str(rcv2) )
		index2 = rcv2.find("PROX STAT READING:")
		if index2 != -1:
			#print("rcv2 len" + str(len(rcv2)) )
			#print("PROX STAT READING: index" + str(index2))
			#print("PROX STAT READING: length" + str(len("PROX STAT READING:")) ) 
			result = rcv2[index2 + len("PROX STAT READING:")]
			#print("result" + result)
			if result == '1' or result == '2' or result == '3' :
				print("Prox Detected on:"+result)
				rcv_again = port.readline().decode('utf-8')
				print(rcv_again)
		else :
			print("decode for PROX STAT READING: error")
	#else :
		#print("decode for KASUN: error")
		#print(rcv)
