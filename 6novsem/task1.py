a = str(input())
b = str(input())

def count_nucleotide(dna, nucleotide):
	counter = dna.count(nucleotide)
	print(counter)
count_nucleotide(a, b)
