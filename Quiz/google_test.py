class EncodedWordDetector:
    def __init__(self, word):
        self.word = word
        self.len_word = len(word)

    def is_encoded(self, test):
        seen = {}
        saw = set()

        if len(test) != self.len_word:
            print("Failed")
            return False

        for x in range(len(self.word)):
            if self.word[x] not in seen:
                if test[x] not in saw:
                    seen[self.word[x]] = test[x]
                    saw.add(test[x])
                else:
                    print("Failed")
                    return False

            else:
                myletter = seen[self.word[x]]
                if myletter != test[x]:
                    print("Failed")
                    return False

        print("Success")
        return True


def main():
    EncodedWord = EncodedWordDetector('banana')
    checkWord = 'xxxxxx'
    EncodedWord.is_encoded(checkWord)


if __name__ == "__main__":
    main()