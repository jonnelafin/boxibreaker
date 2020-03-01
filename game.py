import copy
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
b = "b"
a = "a"
p = "p"
m = "m"
f = "f"
arr = []
co = 0
y = 4
x = 2
future = a
last = a
finals = [[2,1],[3,4],[3,7],[2,10]]
path = []
def burn(arr):
	global finals, f
	for y, x in finals:
		if arr[y][x] == a:
			arr[y][x] = f
def cls():
	print("\033[H\033[J")
def bake(arr):
	out = []
	for i in arr:
		tmp = []
		for z in i:
			tmp.append(z + "")
			#tmp.append(copy.copy(z))
		out.append(tmp)
	return(out)
def init():
	global b,a,p,m,f,arr, x, y, path
	l1 = [b, a, a, b, a, a, b, a, a, b, a, a, b, a, a, a, b]
	l2 = [b, a, a, a, a, a, b, a, a, b, a, a, a, a, a, a, b]
	l3 = [b, a, a, b, a, a, a, a, a, a, a, a, b, a, a, a, b]
	co = 0
	y = 4
	x = 2
	future = a
	last = a
	tmp = []
	for i in range(17):
		tmp.append(b)
	#Construct the array
	arr.append(tmp)
	arr.append(l1)
	arr.append(l2)
	arr.append(l3)
	arr.append(l1)
	arr.append(tmp)
	arr = bake(arr)
	arr[2][1] = f
	arr[2][2] = m
	arr[3][4] = f
	arr[3][5] = m
	arr[3][7] = f
	arr[3][8] = m
	arr[2][10] = f
	arr[2][11] = m
	#set player
#	arr[y][x] = p
	#Test
#	niceP(arr)
def niceP(arr):
	global b, a, p, m, f, x, y, finals, co
	xp = 0
	yp = 0
	arr2 = bake(arr)
	burn(arr2)
	for i in arr2:
		yp = 0
		for z in i:
			p2 = bcolors.HEADER
			end = bcolors.ENDC
			if z == b:
				p2 = bcolors.HEADER
			if z == p:
				p2 = bcolors.FAIL
			if z == m:
				p2 = bcolors.OKBLUE
			if z == m and [xp, yp] in finals:
				p2 = bcolors.OKGREEN
			if z == f:
				p2 = bcolors.WARNING
			if z == a:
				p2 = ""
				end = ""
			z2 = p2 + "█" + end
			print(z2, end="")
			yp = yp + 1
		print("")
		xp = xp + 1
	print("Y: " + str(y) + ", X: " + str(x))
	print(str(co) + " / " + str(len(finals)) + " complete")
def main():
	global b,a,p,m,f,arr
	print("Initialiazing matricies...")
	init()
	print("Done.")
	print("Test print (player should be missing):")
	niceP(arr)
	if input("Start playing? (y/*)\n>") != "y":
		import sys
		sys.exit()
	inp = ""
	while(inp != "q"):
		cls()
		step(inp)
		niceP(arr)
		inp = input(">")
def getVel(c = ""):
	fx = 0
	fy = 0
	if c == "w":
		fy = -1
		fx = 0
	if c == "s":
		fy = 1
		fx = 0
	if c == "a":
		fy = 0
		fx = -1
	if c == "d":
		fy = 0
		fx = 1
	return [fy, fx]
def valid(c = ""):
	global b,a,p,m,f,arr,y,x, future
	out = True
	fy, fx = getVel(c)
	fx2 = fx + x
	fy2 = fy + y
	fc = ""
	try:
		fc2 = arr[fy2+fy][fx2+fx]
	except Exception as e:
		fc2 = a
	try:
		fc = arr[fy2][fx2]
	except Exception as e:
		return False
	future = fc
	if fc == b:
		return False
	if fc == m and (fc2 == b or fc2 == m):
		return False
	return True
finished = False
def step(c = ""):
	global b,a,p,m,f,arr,y,x, future, last, finished, path
	fx = x
	fy = y
	arr[fy][fx] = a
#	burn()
#	last = future
	if(valid(c)):
		path.append([fx,fy])
		fy, fx = getVel(c)
		if future == m:
			arr[fy*2+y][fx*2+x] = m
		fy = fy + y
		fx = fx + x
	x = fx
	y = fy
	arr[fy][fx] = p
	finished = complete()
def complete():
	global arr, finals, co, b
	co2 = 0
	for i in finals:
		if arr[i[0]][i[1]] == m:
			co2 = co2 + 1
	co = co2
	if co == len(finals):
		return True
	return False
if __name__ == "__main__":
	main()
