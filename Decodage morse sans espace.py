alphabet ={
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

def decompose_morse(word, alpha=None):
	if alpha is None:
		alpha = alphabet
	rev_alpha = {v:k for k, v in alpha.items()}
	letters = list(sorted(alpha.values()))

	options = [([], 0)]
	addition = 1
	while addition > 0:
		addition = 0
		new_options = []
		for stack, pos in options:
			if pos == len(word):
				new_options.append((stack, pos))
			else:
				prefix = word[pos:]
				for w in letters:
					if prefix.startswith(w):
						path = stack.copy()
						path.append(w)
						new_options.append((path, pos + len(w)))
						addition += 1
		options = new_options

	unique = set()
	for stack, pos in options:
		if pos != len(word):
			continue
		path = tuple(stack)
		unique.add(''.join(rev_alpha.get(c, c) for c in path))

	return list(sorted(unique))

print(decompose_morse('.--..-.'))