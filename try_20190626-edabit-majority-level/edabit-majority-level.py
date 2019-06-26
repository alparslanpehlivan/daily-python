def majority_vote(lst):
	maxCount = 0
	index = -1  
	for i in range(len(lst)): 

		count = 0
		for j in range(len(lst)): 

				if(lst[i] == lst[j]): 
						count = count + 1


		if(count > maxCount): 

				maxCount = count 
				index = i 


	if (maxCount > len(lst)//2): 
		return lst[index] 

	else: 
		return None