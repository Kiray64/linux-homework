
sequences = []

while True:
	dna_input = input()

	if dna_input == "STOP":
    		break
	
	is_valid = True

	for char in dna_input:
		if char not in "ATGC":
			is_valid = False
			break
	if is_valid == True:
		sequences.append(dna_input)

print(len(sequences))

lengths = []

for seq in sequences:
	lengths.append(len(seq))


print(lengths)

