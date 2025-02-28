import random, string

nato = {
	"a": "alpha",
	"b": "bravo",
	"c": "charlie",
	"d": "delta",
	"e": "echo",
	"f": "foxtrot",
	"g": "golf",
	"h": "hotel",
	"i": "india",
	"j": "juliet",
	"k": "kilo",
	"l": "lima",
	"m": "mike",
	"n": "november",
	"o": "oscar",
	"p": "papa",
	"q": "quebec",
	"r": "romeo",
	"s": "sierra",
	"t": "tango",
	"u": "uniform",
	"v": "victor",
	"w": "whiskey",
	"x": "x-ray",
	"y": "yankee",
	"z": "zulu",
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
	while len(faa) < 4:  # rng loves making short codes, which exist but aren't terribly useful in this context
		faa = "N"
		faa += str(random.randint(1, 9)) # An N-Number may not begin with zero
		
		version = random.randint(0, 3)
		if version == 0:
			for i in range(0, random.randint(0, 4)):
				faa += str(random.randint(0, 9))
		elif version == 1:
			for i in range(0, random.randint(0, 3)):
				faa += str(random.randint(0, 9))
			faa += random.choice(faaletters)
		elif version == 2:
			for i in range(0, random.randint(0, 2)):
				faa += str(random.randint(0, 9))
			for i in range(0, 2):
				faa += random.choice(faaletters)

	return faa




def natobuild(str):
	outstring = ""
	for chr in str:
		outstring += nato[chr] + " "
        
	return outstring
        


if __name__ == "__main__":

	thingies = "abcdefghijklmnopqrstuvwxyz0123456789"

	while True:
		# str = ""
		# for i in range(0, random.randint(3, 5)):
		# 	str += random.choice(thingies)

		st = faacode()
			
		print (st.upper())
		input()
		
		out = ""
		for i in st:
			out += nato[i.lower()] + " "
			
		print (out.upper())
		input ()



