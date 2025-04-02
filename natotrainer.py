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
	"-": "",
}


def distinctletters(st):
	dc = []
	for c in st:
		# print (dc)
		if c in string.ascii_uppercase:
			if c not in dc:
				dc.append(c)

	return len(dc)




def rc(ch):
	return random.choice(ch)

def rn(l=0, u=9):
	return random.randint(l, u)

def rns(l=0, u=9):
	return str(rn(l, u))

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
	



def faacode():
	faaletters = "ABCDEFGHJKLMNPQRSTUVWXYZ" # no I or O

	faa = ""
	distinctcount = 0

	# rng loves making short codes, which exist but aren't terribly useful here
	# also we need more than one letter to learn
	while len(faa) < 4 or distinctcount < 2:

		faa = "N"
		faa += rns(1, 9) # An N-Number may not begin with zero
		
		version = rn(1, 3)
		if version == 0: # skipping this one because it's not very useful when learning letters
			for i in range(0, rn(0, 4)):
				faa += rns(0, 9)
		elif version == 1:
			for i in range(0, rn(0, 2)): # can go up to 3 but again this is for letters
				faa += rns(0, 9)
			faa += rc(faaletters)
		elif version == 2:
			for i in range(0, rn(0, 2)):
				faa += rns(0, 9)
			for i in range(0, 2):
				faa += rc(faaletters)

		distinctcount = distinctletters(faa)

	return faa, "US aircraft registration"


def cacode():
	return "C-" + rc("FGC") + rl(3), "Canadian aircraft registration"


	



def callsign():
	type = random.randint(0, 9)
	name = ""

	# source: https://en.wikipedia.org/wiki/Amateur_radio_licensing_in_the_United_States
	if type == 0:
		call = rc("KNW") + rns() + rl() + rl()
		name = "US amateur radio, Group A"

	elif type == 1:
		var = random.randint(0, 1)
		if var == 0:
			call = "A" + lr(0, 11)
		else:
			call = rc("KNZ") + rl()
		call += rns() + rl()
		name = "US amateur radio, Group A"

	elif type == 2:
		call = "A" + lr(0, 11) + rns() + rl(2)
		name = "US amateur radio, Group B"

	elif type == 3:
		call = rc("KNW") + rl() + rns() + rl(2)
		name = "US amateur radio, Group B"

	elif type == 4:
		call = rc("KNW") + rns() + rl(3)
		name = "US amateur radio, Group C"

	elif type == 5:
		call = rc(["KL", "NL", "WL", "NP", "WP", "KH", "NH", "WH"]) + rns() + rl(3)
		name = "US amateur radio, Group C"

	elif type == 6:
		call = rc("KW") + rl() + rns() + rl(3)
		name = "US amateur radio, Group D"

	elif type == 7:
		call = "K" + rl() + rns() + rl(3)
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



def getcode(faa = True, call = True, eam = False, ca = True):
	opt = []
	if faa:
		opt.append(faacode)
	if call:
		opt.append(callsign)
	if eam:
		opt.append(eamprefix)
	if ca:
		opt.append(cacode)
	if not faa and not call and not eam and not ca:
		opt.append(faacode)
		opt.append(callsign)
		opt.append(cacode)


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


	



