import game
import random

print("Solving")
it = 10000

mov = ["w","a","s","d"]

steps = 800

bs = 0
bp = []
for i in range(it):
	game.init()
	for s in range(steps):
		c = mov[random.randint(0, len(mov)-1)]
		print(str(i)+", "+str(s)+"("+c+")",end="\r")
		game.step(c)
		if game.co > bs:
			bs = game.co
			print("\n"+str(bs))
			if bs == 4:
				bp = game.path
				break
		#else:
			#print(".", end="")
for i in bp:
	print(i)
