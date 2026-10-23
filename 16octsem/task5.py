reads = [
"ATGCC",
"GCCAA",
"CAAAT",
"TTTGG"]

k = 3

for id1, value1 in enumerate(reads):
	for id2, value2 in enumerate(reads):
		if id1!= id2:
			if value1[-k:] == value2[:k]:
				print(str(id1+1) + " - " + str(id2 + 1))
