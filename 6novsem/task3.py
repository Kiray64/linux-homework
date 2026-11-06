a = input()
b = input()


def is_valid_dna(dna):
	e = enumerate(dna)
	nucl = ["A", "T", "C", "G"]
	if dna == "":
		result = False;
	else:
	
		for id, value in e:
			if value in nucl:
				result = True
			else:
				result = False
				break
		return result

def hamming_distance(s1, s2):
	l1 = len(s1)
	l2 = len(s2)
	i1 = is_valid_dna(s1)
	i2 = is_valid_dna(s2)
	e1 = enumerate(s1)
	e2 = enumerate(s2)
	i = 0
	if l1 == l2 and i1 == True and i2 == True:
		for id1, value1 in e1:
			value2 = s2[id1]
			
			if value1 != value2:
				i += 1
		return i

	else:
		return None

angrybirds = hamming_distance(a, b)

print(angrybirds)		
