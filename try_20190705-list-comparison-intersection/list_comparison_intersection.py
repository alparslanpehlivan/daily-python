def letters(word1, word2):
	s1, s2 = set(word1), set(word2)
	return [''.join(sorted(i)) for i in [s1&s2, s1-s2, s2-s1]]

####

def letters(word1, word2):
	return [''.join(list(sorted(set(word1)& set(word2)))),''.join(list(sorted(set(word1)-set(word2)))),''.join(list(sorted((set(word2)-set(word1)))))]

####

def letters(word1, word2):
    count_common = ''
    count_word2 = ''
    count_word1 = ''
    m = sorted(list(set(word1)))
    n = sorted(list(set(word2)))

    for i in n:
        if i in m:

            count_common += i
        else:
            count_word2 += i
    for j in m:
        if j not in n:
            count_word1 += j
    return [count_common, count_word1, count_word2]

####

def letters(word1, word2):
    a = list(word1)
    b = list(word2)
    c = a + b
    a1 = []
    b1 = []
    c1 = []
    for i in range(len(c)):
        if c[i] in word1 and c[i] in word2:
            if c[i] not in c1:
                c1.append(c[i])
        elif c[i] in word1 and c[i] not in a1:
            a1.append(c[i])
        elif c[i] in word2 and c[i] not in b1:
            b1.append(c[i])
    y = ''.join(sorted(a1))
    z = ''.join(sorted(b1))
    x = ''.join(sorted(c1))

    return [x, y, z]

####

def letters(word1, word2):
	shared=[]
	uniq1=[]
	uniq2=[]
	for i in range(len(word1)):
		if word1[i] in word2:
			shared.append(word1[i])
		else:
			uniq1.append(word1[i])
	shared=sorted(list(set(shared)))
	uniq1=sorted(list(set(uniq1)))
	uniq2=[word2[i] for i in range(len(word2)) if word2[i] not in word1]
	uniq2=sorted(list(set(uniq2)))
	return [''.join(shared),''.join(uniq1),''.join(uniq2)]
