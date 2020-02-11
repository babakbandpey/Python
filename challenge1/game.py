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
	return data.replace("be", "python")

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
	for person in data.split(","):
		tmp = person.split(":")
		result.append((tmp[0], tmp[1]))
	return result
	
# Return the dictionary with the entry for "192.168.1.243" removed
def myAnswer15(data):
	data.pop("192.168.1.243")
	return data

#The answer is the sentence where each word is in reverese (the words keep their place in the sentence)
def myAnswer16(data):
	return " ".join(word[::-1] for word in data.split(" "))

#return a list containing 10 tuples of the ones found in data
def myAnswer17(data):
	return [('x', 'y')] * 10

#Add a new item to the dictionary with the key "yellow" and the value 22
def myAnswer18(data):
	data["yellow"] = 22
	return data

# return a set containing all unique ip addresses in data
def myAnswer19(data):
	import re
	return set(re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})', data))

# return a dictionary containing all status codes (in string)  as key, and how many times their occured (in int) as value
def myAnswer20(data):
	from collections import Counter
	return dict(Counter([line.split(" ")[-2] for line in data.strip().split("\n")]))

# return the average size (in int) of all responses with status 200 
def myAnswer21(data):
	tmp = [int(line.split(" ")[-1]) for line in data.strip().split("\n") if " 200 " in line]
	return int(sum(tmp)/len(tmp))

# return the number of times (in int)  an images of the type png is in the response
def myAnswer22(data):
	return len([line for line in data.strip().split("\n") if " 200 " in line and ".png " in line])

# convert this list to a dictionary where the episode number is the key (ie: "Episode I") and the name is the value (ie: "The Phantom Menace")
def myAnswer23(data):
	return {value:key for (key, value) in data}

# return a sorted list (in int) containing the numbers 1-100, but without the numbers divideble with the number in data (ie. the numbers 3,6,9,12... should not be there)
def myAnswer24(data):
	return [x for x in range(101) if x % int(data) != 0]

# this sha1 hash was found. the system it comes from normally uses 4 character kodes, consisting of a-z in lowercase
def myAnswer25(data):
	from hashlib import sha1
	def decrypt(encrypted, max_depth, current_depth = 0, text = ""):
		if(current_depth < max_depth):
			for alpha in range(ord("a"), ord("z")+1):
				if sha1(str(text + chr(alpha)).encode('utf-8')).hexdigest() == encrypted:
					return text + chr(alpha)
				else:
					current_depth += 1
					result = decrypt(encrypted, max_depth, current_depth, text + chr(alpha))
					if(result != None and result != ""):
						return result
					current_depth -= 1
		else:
			return ""

	return decrypt(data, 4)

# the data provided contains a tuple, where first element is a sha256. The second element contains a dictionary (created by scapping the victims facebook) of words an values that the password could be generated from. Assume that the password length is 8 characters, and that the system requires lowercase, uppercase letters and numbers.
def myAnswer26(data):
	print(data)
	from hashlib import sha256
	hash256, arr = data
	print(hash256, arr)

	words = []

	for x in arr:
		if(type(x) != str):	
			words += list(x) + [s.title() for s in list(x) if s.isalpha()]
		else:
			words.append(x)
			words.append(x.title())


	words = list(set([s for s in words if len(s) < 8]))

	print(words)


	def decrypt(encrypted, words, text = ""):
		if(len(text) >= 8):
			return ""

		for x in range(len(words)):
			if len(text + words[x]) > 8 :
				continue
			
			print(str(text + words[x]), sha256(str(text + words[x]).encode('utf-8')).hexdigest())

			if sha256(str(text + words[x]).encode('utf-8')).hexdigest() == encrypted:
				print("----------------------- FOUND ------------------------")
				return str(text + words[x])
			else:
				result = decrypt(encrypted, words, str(text + words[x]))
				if(result != None and result != ""):
					print("=======================   ", result)
					return result

		return ""

	return decrypt(hash256, words)
	

for question_number in range(26, 27):
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
	elif question_number == 15:		
		game.answer(question_number, myAnswer15(game.data(question_number)))
	elif question_number == 16:		
		game.answer(question_number, myAnswer16(game.data(question_number)))
	elif question_number == 17:		
		game.answer(question_number, myAnswer17(game.data(question_number)))
	elif question_number == 17:		
		game.answer(question_number, myAnswer17(game.data(question_number)))
	elif question_number == 18:		
		game.answer(question_number, myAnswer18(game.data(question_number)))
	elif question_number == 19:		
		game.answer(question_number, myAnswer19(game.data(question_number)))
	elif question_number == 20:		
		game.answer(question_number, myAnswer20(game.data(question_number)))
	elif question_number == 21:		
		game.answer(question_number, myAnswer21(game.data(question_number)))
	elif question_number == 22:
		game.answer(question_number, myAnswer22(game.data(question_number)))
	elif question_number == 23:
		game.answer(question_number, myAnswer23(game.data(question_number)))
	elif question_number == 24:
		game.answer(question_number, myAnswer24(game.data(question_number)))
	elif question_number == 25:
		game.answer(question_number, myAnswer25(game.data(question_number)))
	elif question_number == 26:
		game.answer(question_number, myAnswer26(game.data(question_number)))



