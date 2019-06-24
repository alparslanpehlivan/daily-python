def progress_days(runs):
	count=0
	for i in range(0,len(runs)-1):
		if runs[i+1] > runs[i]:
			count = count + 1
		else:
			continue
	return count