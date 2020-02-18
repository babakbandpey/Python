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

