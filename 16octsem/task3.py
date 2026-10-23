rna = input()

coding_count = 0

for i in range(0, len(rna), 3):
	cod = rna[i:i+3]
	
	if cod in ["UAA", "UAG", "UGA"]:
		print("Количество кодирующих кодонов:", coding_count)
		print("Стоп-кодон:", cod)
		break
	else:
		coding_count += 1
