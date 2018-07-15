class RollingHash:
	def __init__(self, string, size):
		self.str  = string
		self.hash = 0

		for i in range(0, size):
			self.hash += ord(self.str[i])

		self.init = 0
		self.end  = size

	def update(self):
		if self.end <= len(self.str) -1:
			self.hash -= ord(self.str[self.init])
			self.hash += ord(self.str[self.end])
			self.init += 1
			self.end  += 1

	def digest(self):
		return self.hash

	def text(self):
		return self.str[self.init:self.end]



def rabin_karp(substring, string):

	if substring == None or string == None:
		return
	if substring == "" or string == "":
		return

	if len(substring) > len(string):
		return

	hs 	 = RollingHash(string, len(substring))
	hsub = RollingHash(substring, len(substring))
	hsub.update()

	for i in range(len(string)-len(substring)+1):
		if hs.digest() == hsub.digest():
			if hs.text() == substring:
				print("Found in Position %d" % i)
		hs.update()

	return

def main():
    T = "CATATCGGCATA"
    P = "ATA"
    print ("Looking for pattern ' + %s + ' in text ' + %s + ':\n" % (P,T))
    rabin_karp(P,T)


if __name__ == "__main__":
    main()