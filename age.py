#!/usr/bin/python3


run = True
year = 2020

while(run):
	try:
		age = int(input("Hvor gammel er du? "))
		print("du bliver " + str(100 + age) + " i aar: " + str(year + 100))

		print("du bliver 100 i aar: " + str(100 - age + year))

		print("du bliver 100 i aar: {}".format( 100 - age + year))
		print("you will be {1} years old, in 100 years. And now is {0}".format(year,  age + 100)
		print("you will be %d years old, in 100 years." % (age + 100))

		run = False
	except:
		print("Tast kun tal mellem 0 og 1000")
		
