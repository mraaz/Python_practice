def main():
    dictionary = ("GEEKS", "FOR", "QUIZ", "GO")
    boggle = {'G': ('I', 'E', 'U'),
              'I': ('G', 'Z', 'U', 'E', 'K'),
              'Z': ('E', 'K', 'I'),
              'U': ('G', 'E', 'I'),
              'E': ('G', 'I', 'K', 'S', 'Q', '2E', 'Z', 'U'),
              'K': ('Z', 'E', 'S', '2E', 'I'),
              'Q': ('U', 'E', 'S'),
              'S': ('Q', 'E', '2E', 'U', 'K'),
              '2E': ('S', 'E', 'K'),
              }

    """    
               ('G','I','Z'),
               ('U','E','K'),
               ('Q','S','E')
    """

    def FindWord(word,myword):
        if word[0] in boggle:
            if len(word) > 1:
                myset = boggle[word[0]]
                if word[1] in myset:
                    FindWord(word[1:], myword)
            else:
                print("We found the word!! %s" % myword)
                return

        else:

            return


    for words in dictionary:
        if len(words) > 1:
            FindWord(words, words)

        else:
            print("Check for one letter in Boggle")


if __name__ == "__main__":
    main()