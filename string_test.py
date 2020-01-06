string = "KASUN:PROX STAT READING 0"
#string = "PROX STAT READING 0"
#print(string)
index = string.find("KASUN")
#print(index)
if index != -1 :
	print("KASUN found")
	print(string[index + len("KASUN"): ])
else :
	print("KASUN not found")
