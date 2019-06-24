def power_ranger(power, minimum, maximum):
	count=0
	for i in range(1,maximum+1):
		k=i**power
		if k <= maximum and k >= minimum:
			count = count +1
		if k>maximum:
			break
	return count