#!/usr/bin/python3


def hr():
	print("--------------------------------------------------------------------------------------")

x = [1, 3, -7, 4, 9, -5, 4]
print("X is the following array: ", x)

for i in range(len(x)):
	if(x[i] < 0):
		print("Found negative number {1} in index {0}".format(i, x[i]))


print("All even numbers from 0 tp 1000: ")
print(list(range(0, 1001, 2)))


tuples = [(80, 81), (20, 21)]
print("Example of looping a list of tuples: ", tuples)

for _, second_value in tuples:
	print("the second value is: {0}".format(second_value))

hr()


for x in range(1,11):
	for y in range(1,11):
		print(x*y, end="\t")
	print("")


hr()

l = [x*y for x in range(1, 11) for y in range(1, 11)]
print(l)

hr()


letters = range(ord("a"), ord("d"))
print(letters)
for a in letters:
	for b in letters:
		for c in letters:
			print(chr(a),chr(b),chr(c), end=", ")
		print(" ")
 
hr()

l = [chr(a)+chr(b)+chr(c) for a in letters for b in letters for c in letters]
print(l)

hr()



