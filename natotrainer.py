import random, string

nato = {
	"A": "alpha",
	"B": "bravo",
	"C": "charlie",
	"D": "delta",
	"E": "echo",
	"F": "foxtrot",
	"G": "golf",
	"H": "hotel",
	"I": "india",
	"J": "juliet",
	"K": "kilo",
	"L": "lima",
	"M": "mike",
	"N": "november",
	"O": "oscar",
	"P": "papa",
	"Q": "quebec",
	"R": "romeo",
	"S": "sierra",
	"T": "tango",
	"U": "uniform",
	"V": "victor",
	"W": "whiskey",
	"X": "x-ray",
	"Y": "yankee",
	"Z": "zulu",
	"0": "zero",
	"1": "one",
	"2": "two",
	"3": "three",
	"4": "four",
	"5": "five",
	"6": "six",
	"7": "seven",
	"8": "eight",
	"9": "niner",
}




def faacode():
	faaletters = "ABCDEFGHJKLMNPQRSTUVWXYZ" # no I or O

	faa = ""
	while len(faa) < 4: # rng loves making short codes, which exist but aren't terribly useful here
		faa = "N"
		faa += str(random.randint(1, 9)) # An N-Number may not begin with zero
		
		version = random.randint(1, 3)
		if version == 0: # skipping this one because it's not very useful when learning letters
			for i in range(0, random.randint(0, 4)):
				faa += str(random.randint(0, 9))
		elif version == 1:
			for i in range(0, random.randint(0, 2)): # can go up to 3 but again this is for letters
				faa += str(random.randint(0, 9))
			faa += random.choice(faaletters)
		elif version == 2:
			for i in range(0, random.randint(0, 2)):
				faa += str(random.randint(0, 9))
			for i in range(0, 2):
				faa += random.choice(faaletters)

	return faa, "US aircraft registration"


def rc(ch):
	return random.choice(ch)

def rn(l=0, u=9):
	return str(random.randint(l, u))

def rl(count = 1):
	s = ""
	for i in range(0, count):
		s += random.choice(string.ascii_uppercase)
	return s

def lr(l="A", u="Z"):
	return string.ascii_uppercase[(random.randint(l, u))]

def onein(max, yea, nay):
	if random.randint(0, max) == 0:
		return yea
	else:
		return nay
	



def callsign():
	type = random.randint(0, 9)
	name = ""

	# source: https://en.wikipedia.org/wiki/Amateur_radio_licensing_in_the_United_States
	if type == 0:
		call = rc("KNW") + rn() + rl() + rl()
		name = "US amateur radio, Group A"

	elif type == 1:
		var = random.randint(0, 1)
		if var == 0:
			call = "A" + lr(0, 11)
		else:
			call = rc("KNZ") + rl()
		call += rn() + rl()
		name = "US amateur radio, Group A"

	elif type == 2:
		call = "A" + lr(0, 11) + rn() + rl(2)
		name = "US amateur radio, Group B"

	elif type == 3:
		call = rc("KNW") + rl() + rn() + rl(2)
		name = "US amateur radio, Group B"

	elif type == 4:
		call = rc("KNW") + rn() + rl(3)
		name = "US amateur radio, Group C"

	elif type == 5:
		call = rc(["KL", "NL", "WL", "NP", "WP", "KH", "NH", "WH"]) + rn () + rl(3)
		name = "US amateur radio, Group C"

	elif type == 6:
		call = rc("KW") + rl() + rn() + rl(3)
		name = "US amateur radio, Group D"

	elif type == 7:
		call = "K" + rl() + rn() + rl(3)
		name = "US amateur radio, Group D"

	elif type == 8:
		call = "W" + onein(11, rl(2), rl(3))
		name = "US commercial broadcast east"

	elif type == 9:
		call = "K" + onein(11, rl(2), rl(3))
		name = "US commercial broadcast west"

	return call, name



def eamprefix():
	possible = string.ascii_uppercase + "234567"
	st = ""
	for i in range(0, 6):
		st += random.choice(possible)

	return st, "Emergency Action Message preamble"




def natobuild(st):
	outstring = ""
	for chr in st:
		outstring += nato[chr] + " "
        
	return outstring



def getcode(faa = True, call = True, eam = False):
	opt = []
	if faa:
		opt.append(faacode)
	if call:
		opt.append(callsign)
	if eam:
		opt.append(eamprefix)
	if not faa and not call and not eam:
		opt.append(faacode)
		opt.append(callsign)

	st, name = random.choice(opt)()
	out = natobuild(st)
		
	return (st, out, name)

        


if __name__ == "__main__":
	while True:
		code = getcode()
		print (code[0])
		input()
		print (code[1])
		input()


	



