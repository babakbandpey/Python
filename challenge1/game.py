#!/usr/bin/python3

import challenge

game = challenge.client(ip_address="cybergame.dk", port=39594)

game.login("baba0117", "baba0117")

# Resend the text that is submitted in data as the answer
def myAnswer0(data):
	return data

# The answer is the data multiplied with 2
def myAnswer1(data):
	return data * 2

# The answer is the data in uppercase
def myAnswer2(data):
	return data.upper()

# Return the text in data in the reverse order
def myAnswer3(data):
	return data[::-1]

# Return the sorted list
def myAnswer4(data):
	data.sort()
	return data

# Return a list containing only the first 3 elements
def myAnswer5(data):
	return data[0:3]


def multiplyWithFive(n):
	return n*5

# Return a list where each number is multiplied with 5
def myAnswer6(data):
	return list(map(multiplyWithFive, data))


# Return the value of the 6th element
def myAnswer7(data):
	return data[5]

# Return a sorted list, where the duplicates are removed
def myAnswer8(data):
	data = set(data)
	data = list(data)
	data.sort()
	return data

# Replace 'be' in the data with 'python'

def myAnswer9(data):
	data = data.replace("be", "python")
	return data

# The answer is the whole sentence with the word 'star' spelled backwards
def myAnswer10(data):
	data = data.replace("staring", "****")
	data = data.replace("star", "rats")
	data = data.replace("****", "staring")
	return data

# Return a list containing 20 values starting with the number in data and incrementing with 5
def myAnswer11(data):
	result = [data]
	print(result)
	for x in range(1, 20):
		result.append(result[x-1] + 5)
	return result

# The data is a list of tuples containing ip-addresses and number of connections. return the number of connections for ip-address 192.168.1.212
def myAnswer12(data):
	print(data)
	for t in data:
		t = list(t)
		if(t[0] == "192.168.1.212"):
			return t[1]

# The answer is the total sum of all the numbers in the list
def myAnswer13(data):
	return sum(data)	

# Return a list containing tuples with names and phonenumbers [("name1","phone1"),("name2","phone2")...]
def myAnswer14(data):
	result = []
	data = data.split(",")
	for person in data:
		tmp = person.split(":")
		result.append((tmp[0], tmp[1]))
	return result
	
for question_number in range(14, 28):
	game.question(question_number)
	if question_number == 0:		
		game.answer(question_number, myAnswer0(game.data(question_number)))
	elif question_number == 1:		
		game.answer(question_number, myAnswer1(game.data(question_number)))
	elif question_number == 2:		
		game.answer(question_number, myAnswer2(game.data(question_number)))
	elif question_number == 3:		
		game.answer(question_number, myAnswer3(game.data(question_number)))
	elif question_number == 4:		
		game.answer(question_number, myAnswer4(game.data(question_number)))
	elif question_number == 5:		
		game.answer(question_number, myAnswer5(game.data(question_number)))
	elif question_number == 6:		
		game.answer(question_number, myAnswer6(game.data(question_number)))
	elif question_number == 7:		
		game.answer(question_number, myAnswer7(game.data(question_number)))
	elif question_number == 8:		
		game.answer(question_number, myAnswer8(game.data(question_number)))
	elif question_number == 9:		
		game.answer(question_number, myAnswer9(game.data(question_number)))
	elif question_number == 10:		
		game.answer(question_number, myAnswer10(game.data(question_number)))
	elif question_number == 11:		
		game.answer(question_number, myAnswer11(game.data(question_number)))
	elif question_number == 12:		
		game.answer(question_number, myAnswer12(game.data(question_number)))
	elif question_number == 13:		
		game.answer(question_number, myAnswer13(game.data(question_number)))
	elif question_number == 14:		
		game.answer(question_number, myAnswer14(game.data(question_number)))





