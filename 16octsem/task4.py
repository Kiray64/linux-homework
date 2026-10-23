growth = [[0, 2, 4, 8],
    [0, 1, 1, 2],
    [0, 3, 6, 9]]

x = 5

for culture in growth:
	for id, value in enumerate(culture):
	        if value >= x:
        		print(id)
            		break
    	else:
       		print("отсутствует")
