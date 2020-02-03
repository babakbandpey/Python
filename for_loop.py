#!/usr/bin/python3

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


for x in list(range(1,11)):
	for y in list(range(1,11)):
		print(x*y, end="\t")
	print("")
