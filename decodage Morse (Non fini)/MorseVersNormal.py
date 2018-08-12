#class inventaire:
#	def __init__(self, phrase):
#		self.phrase = phrase
morseAlphabet ={
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--.."
    }
compte = 0		
passagerie = {}
NombreDeCaractere = {}
DebutPhrase = {}
Phrase = {}
		
def passage(n):
	if ".-" == symbole:
#		print("A")
		lettre = "A"
	elif "-..." == symbole:
#		print("B")
		lettre = "B"
	elif "-.-." == symbole:
#		print("C")
		lettre = "C"
	elif "-.." == symbole:
#		print("D")
		lettre = "D"
	elif "." == symbole:
#		print("E")
		lettre = "E"
	elif "..-." == symbole:
#		print("F")
		lettre = "F"
	elif "--." == symbole:
#		print("G")
		lettre = "G"
	elif "...." == symbole:
#		print("H")
		lettre = "H"
	elif ".." == symbole:
#		print("I")
		lettre = "I"
	elif ".---" == symbole:
#		print("J")
		lettre = "J"
	elif "-.-" == symbole:
#		print("K")
		lettre = "K"
	elif ".-.." == symbole:
#		print("L")
		lettre = "L"
	elif "--" == symbole:
#		print("M")
		lettre = "M"	
	elif "-." == symbole:
#		print("N")
		lettre = "N"
	elif "---" == symbole:
#		print("O")
		lettre = "O"
	elif ".--." == symbole:
#		print("P")
		lettre = "P"
	elif "--.-" == symbole:
#		print("Q")
		lettre = "Q"
	elif ".-." == symbole:
#		print("R")
		lettre = "R"
	elif "..." == symbole:
#		print("S")
		lettre = "S"
	elif "-" == symbole:
#		print("T")
		lettre = "T"
	elif "..-" == symbole:
#		print("U")
		lettre = "U"
	elif "...-" == symbole:
#		print("V")
		lettre = "V"
	elif ".--" == symbole:
#		print("W")
		lettre = "W"
	elif "-..-" == symbole:
#		print("X")
		lettre = "X"	
	elif "-.--" == symbole:
#		print("Y")
		lettre = "Y"
	elif "--.." == symbole:
#		print("Z")
		lettre = "Z"		
	else:
		return
		
	AttributionTaille(lettre)	
#	print(lettre)Mark Morrison
	return AttributionPassage(n, lettre)
	
def AttributionPassage(param1, param2):
	try:
		passagerie['PASSAGE '+ str(param1)].append(param2)
	except KeyError:
		passagerie['PASSAGE '+ str(param1)] = [param2]
	return
	
def CreationPremiereLettre(h = 1):
	for item in passagerie['PASSAGE '+ "1"]:
		DebutPhrase["PremiereLettre "+ str(h)] = [item]
		h += 1
		
def AttributionTaille(n):
	try:
		if n not in NombreDeCaractere['Taille  '+ str(len(symbole))]: 
			NombreDeCaractere['Taille  '+ str(len(symbole))].append(n)
		else:
			pass
	except KeyError:
		NombreDeCaractere['Taille  '+ str(len(symbole))] = [n]
	return
	

def Classement(positionInLib = 1):
	for tour in range(1, len(passagerie)+1):
		for item in passagerie['PASSAGE '+ str(tour)]:
			for indice in range(0, len(passagerie['PASSAGE '+ str(positionInLib)])):
	       		if item in NombreDeCaractere['Taille  '+ str(indice)]:
		      		try:
						Phrase["Phrase "+ str(h)].append(item)
					except KeyError:
						Phrase["Phrase "+ str(h)] = DebutPhrase["PremiereLettre "+ str(o)]
						
				if len(morseAlphabet[item])
					
	return
	
#def attribution(param1, param2):
#	if param1 in liste1:
#		rangement1.append(param2)
#	elif param1 in liste2:
#		rangement2.append(param2)
#	elif param1 in liste3:
#		rangement3.append(param2)
#	elif param1 in liste4:
#		rangement4.append(param2)
#
#	return 

#def rangement(n):
#	for t in range(1, n+1, 4):
#		liste1.append(t)
#	for t in range(2, n+1, 4):
#		liste2.append(t)
#	for t in range(3, n+1, 4):
#		liste3.append(t)
#	for t in range(4, n+1, 4):
#		liste4.append(t)
#	return

#def CreationPhrase(n):
##	tour = 0
##	while tour != n:
#	for i in range(10):
#		try:
#			possibilite['Phrase '+ str(i)].append(rangement1[i])
#		except IndexError:
#			return		
#		except KeyError:
#			possibilite['Phrase '+str(i)] = [rangement1[i]]
##		tour += 1
	
	
enter = input("< ")
message = list(enter)
message2 = message.copy()
CreationSymbole = []
#liste1 = []
#liste2 = []
#liste3 = []
#liste4 = []
#rangement1 = []
#rangement2 = []
#rangement3 = []
#rangement4 = []
#phrase = []
k = 1
print(list(enter))
#rangement(len(message))
while k != len(list(enter))+1:
#	print("PASSAGE N°", k)
	for i in range(len(message)):
#		print("passage n°", k, "  sous-passage n°", i)
		CreationSymbole += message[i]
		symbole = ''.join(CreationSymbole)
		passage(k)
	CreationSymbole = []
	del message[0]
	k += 1
CreationPremiereLettre()
Classement()

print(passagerie)
print("\n", NombreDeCaractere)
print("\n", Phrase)
#CreationPhrase(len(message2))
#print(possibilite)		
#print(liste1)
#print(liste2) 
#print(liste3) 
#print(liste4) 
#print(rangement1) 
#print(rangement2) 
#print(rangement3) 
#print(rangement4)
