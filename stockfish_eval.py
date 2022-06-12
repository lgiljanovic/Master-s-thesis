#!/usr/bin/python3.8

from stockfish import Stockfish
import threading

def evaluate(file_to_read, file_to_write, start_from):

	stockfish = Stockfish("/usr/games/stockfish", 
						parameters={"Threads": 1, "Minimum Thinking Time": 3000})
	current = 0
	with open(file_to_read, 'r') as file:
		with open(file_to_write, 'a') as fens_file:
			for fen in file:
				if start_from > current:
					current += 1
					continue

				fen = fen[:-1]	
				stockfish.set_fen_position(fen)
				result = stockfish.get_evaluation()

				# If result type is mate, write 1000/-1000 depending on value.
				# 1000 indicates that white won and -1000 than black won.
				if result["type"] == "mate":
					if result["value"] < 0:
						fens_file.write(fen + " : " + str(-1000) + "\n")
					else:
						fens_file.write(fen + " : " + str(1000) + "\n")
				else:
					fens_file.write(fen + " : " + str(round(result["value"] / 100.0, 2)) + "\n")
				current += 1
				print(current)

	file.close()
	fens_file.close()


def load_data(file_to_read, file_to_write, from_, to):
	current = 0
	with open(file_to_read, 'r') as file:
		with open(file_to_write, 'w') as fens_file:
			for fen in file:
				if current >= to:
					break
				if from_ > current:
					current += 1
					continue

				fens_file.write(fen[:-1] + "\n")
				current += 1
	file.close()
	fens_file.close()			




load_data('/home/luka/Downloads/fens_no_duplicates.txt', 'fen1.txt', 2000000, 2003000)
load_data('/home/luka/Downloads/fens_no_duplicates.txt', 'fen2.txt', 2003001, 2006000)
load_data('/home/luka/Downloads/fens_no_duplicates.txt', 'fen3.txt', 2006001, 2010000)
load_data('/home/luka/Downloads/fens_no_duplicates.txt', 'fen4.txt', 2010001, 2014000)
load_data('/home/luka/Downloads/fens_no_duplicates.txt', 'fen5.txt', 2014001, 2018000)
load_data('/home/luka/Downloads/fens_no_duplicates.txt', 'fen6.txt', 4033001, 4036000)
load_data('/home/luka/Downloads/fens_no_duplicates.txt', 'fen7.txt', 4036001, 4039000)

load_data('/home/luka/Downloads/fens_no_duplicates.txt', 'fen8.txt', 4039001, 4042000)

print('Data loaded', end='\n')


# creating thread 
t1 = threading.Thread(target=evaluate, args=('fen1.txt','fens1w.txt', 0))
t2 = threading.Thread(target=evaluate, args=('fen2.txt','fens2w.txt', 0))
t3 = threading.Thread(target=evaluate, args=('fen3.txt','fens3w.txt', 0))
t4 = threading.Thread(target=evaluate, args=('fen4.txt','fens4w.txt', 0))
t5 = threading.Thread(target=evaluate, args=('fen5.txt','fens5w.txt', 0))
t6 = threading.Thread(target=evaluate, args=('fen6.txt','fens6w.txt', 0))
t7 = threading.Thread(target=evaluate, args=('fen7.txt','fens7w.txt', 0))
t8 = threading.Thread(target=evaluate, args=('fen8.txt','fens8w.txt', 0))

t1.start() 
t2.start() 
t3.start() 
t4.start() 
t5.start() 
t6.start() 
t7.start() 
t8.start() 

t1.join() 
t2.join() 
t3.join() 
t4.join()
t5.join() 
t6.join() 
t7.join() 
t8.join()

print("Done!")	 
