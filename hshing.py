#!/usr/bin/python3
from hashlib import sha1

def sha(rng):
	for alpha in rng:
		print(sha1(str(chr(alpha)).encode('utf-8')).hexdigest(), chr(alpha))


# ha(range(ord("a"), ord("z")+1))
# sha(range(ord("A"), ord("Z")+1))
# sha(range(256))

import itertools as it

for i in range(7):
	ls = it.permutations(['1', '!', '6', '&', '0', '=', '+', '?', 'd', 'D', 'm', 'M'], i)
	for x in ls:
		print(x)
		print("".join(list(x)))
		if sha1("".join(list(x)).encode('utf-8')).hexdigest() == '29325ad40aa35e83fb2066d10c7c75122c082205':
			print("----------------------- FOUND ------------------------")
			print("".join(list(x)))
			break


def brut(data):
	print(data)
	from hashlib import sha1
	hash256, words = data
	print(hash256, len(hash256), words)

	import re

	def decrypt(encrypted, words, text = ""):
		if(len(text) >= 6):
			return ""

		for x in range(len(words)):
			to_hash = text + words[x]
			if len(to_hash) > 6:
				continue

			# print(to_hash, sha1(to_hash.encode('utf-8')).hexdigest(), len(sha1(to_hash.encode('utf-8')).hexdigest()))

			if sha1(to_hash.encode('utf-8')).hexdigest() == encrypted:
				print("----------------------- FOUND ------------------------")
				return to_hash
			else:
				result = decrypt(encrypted, words, to_hash)
				if(result != None and result != ""):
					print("=======================   ", result)
					return result

		return ""

	return decrypt(hash256, words)


# print(brut(['29325ad40aa35e83fb2066d10c7c75122c082205', ['1', '!', '6', '&', '0', '=', '+', '?', 'd', 'D', 'm', 'M']]))
