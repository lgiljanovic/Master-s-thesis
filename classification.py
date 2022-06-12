#!/usr/bin/python3.8

# output je: pobjeda remi poraz
# npr. 1 0 0 za pobjedu

with open('fens.txt', 'r') as file:
	with open('fens_final_classification.txt', 'w') as fens_file:
		for line in file:
			line = line.strip()
			print(line)
			line = line.split(':')
			fen = line[0].strip()
			score = float(line[1].strip())
			if score > 1:
				fens_file.write(fen + " : 1 0 0\n")	
			elif score < -1:
				fens_file.write(fen + " : 0 0 1\n")
			else:
				fens_file.write(fen + " : 0 1 0\n")

file.close()
fens_file.close()
