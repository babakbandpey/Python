#!/usr/bin/python3


alpha = range(ord("A"), ord("Z")+1)

# Ceasar Cipher

for x in alpha:
	print(chr(x), end = "; ")
print("")

for x in alpha[5:]:
	print(chr(x), end = "; ")
print("")

def create_ceaser_wheel(displacement = 0):
	global alpha
	wheel = {" ": " "}
	
	index = 0
	for x in alpha[displacement:]:
		wheel[chr(alpha[index])] = chr(x)
		index += 1

	for x in alpha[0:displacement]:
		wheel[chr(alpha[index])]  = chr(x)
		index += 1

	return wheel

def encrypt(text, displacement):
	wheel = create_ceaser_wheel(displacement)
	for l in text:
		print(wheel[l.upper()], end = " " )
	print("")

print(create_ceaser_wheel(10))



text = input("Type some text to be encrypted: ")

for x in range(0,40):
	encrypt(text, x)


