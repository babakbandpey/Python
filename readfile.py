#!/usr/bin/python3

try:
	file_object = open("./age.py", "r")
	key_word = input("Search for some text in age.py file: ")
	line_number = 0
	for line in file_object:
		line_number +=1
		if( key_word in line):
			print("{0} is found in line {1}, line number: {2}".format(key_word, line, line_number))

	file_object.close()

except:
	print("File could not open") 
