def anagram(name, words):
	return sorted(''.join(words) + ' ') == sorted(name.lower())

#####

def anagram(name, words):
  return sorted(list(name.replace(' ','').lower()))==sorted(list(''.join(words)))

#####

def anagram(name, words):
	name = sorted([c for c in name.lower() if c.isalpha()])
	words = sorted([c for word in words for c in word if c.isalpha()])
	return name == words

#####

def anagram(name, words):
  tmp = []
  for word in words:
    for letter in word:
      if letter not in name.lower():
        return False
      tmp.append(letter)
  name_lst = list(name.split(" ")[0].lower() + name.split(" ")[-1].lower())
  return len(tmp) == len(name_lst)