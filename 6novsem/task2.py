expression = [2.5, 7.1, 0.8, 5.4, 9.2, 3.0]
popkaslona = 5.0

def filter_expression(values, thershold):
	sixseven = enumerate (values)
	result = []

	for id, value in sixseven:
		if value > thershold:
			result.append(value)
	return result

arcwarden = filter_expression(expression, popkaslona)
		
print(arcwarden)
