reference = input()
sample = input()

for pose, base in enumerate(reference, start = 1):
	if base != sample[pose - 1]:
		print(str(pose) + ": " + base + " > " + sample[pose - 1])
