def majority_vote(lst):
	for i in range(len(lst)):
		if lst.count(lst[i]) > len(lst) / 2:
			return lst[i] 
