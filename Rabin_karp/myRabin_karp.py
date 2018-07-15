class Hash:
    def __init__(self, string, size):
        self.str = string
        self.hash = 0

        i = 1

        while i <= size:
            self.hash += 101**(size-i) * ord(self.str[i-1])
            i += 1


    def rollhash(self, remChar, insChar, size):
        self.hash = self.hash - (101**(size-1) * ord(remChar))
        self.hash *= 101
        self.hash += 101**0 * ord(insChar)


def rabin_karp(string, substring):
    i = len(string)
    j = len(substring)

    hs = Hash(string, j)
    hsub = Hash(substring, j)

    if j > i or i == 0 or j == 0:
        print("Error, invalid string")
        return

    for x in range(i-j+1):
        if hs.hash == hsub.hash:
            if string[x:x+j] == substring:
                print("Found string in position %d" % x)

        if x < i-j:
            hs.rollhash(string[x], string[x+j], j)

    print ("All Done")


if __name__ == "__main__":
    myString = "Hello world, we are all here, in this world"
    string_to_search = "world"

    rabin_karp(myString.lower(), string_to_search.lower())