your_list = 'abaa'
lib = {"a" : 1, "b" : 2}
complete_list = []
liste = []

for current in list(range(2**(len(your_list)-1))):
	a = [i for i in your_list]
	for y in list(range(current)):
		a = list(set([x+i for i in your_list for x in a]))
	complete_list += a
	
for item in range(len(complete_list)):
	compte = 0
	for item2 in complete_list[item]:
		compte += lib[item2]
	if compte <= 4 and complete_list[item] not in liste:
			liste.append(complete_list[item])
	else:
		pass
print(complete_list, "\n\n")
print(liste)
