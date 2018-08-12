Enter = 'abaa'
lib = {"a" : 1, "b" : 2}
List_De_Passage = []
liste = []

for current in list(range(2**(len(Enter)-1))):
	a = [i for i in Enter]
	for y in list(range(current)):
		a = list(set([x+i for i in Enter for x in a]))
	List_De_Passage += a
	
for item in range(len(List_De_Passage)):
	compte = 0
	for item2 in List_De_Passage[item]:
		compte += lib[item2]
	if compte <= 4 and List_De_Passage[item] not in liste:
			liste.append(List_De_Passage[item])
	else:
		pass
print(List_De_Passage, "\n\n")
print(liste)
