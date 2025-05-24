import re
import sys

n, m = map(int, sys.stdin.readline().split())

class HashTable:
    def __init__(self, size=2000):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return sum(ord(c) for c in key) % self.size

    def add(self, key):
        key = key.lower()
        index = self._hash(key)
        if self.cont(key):
            return
        node = (key, self.table[index])
        self.table[index] = node

    def cont(self, key):
        key = key.lower()
        index = self._hash(key)
        curr = self.table[index]
        while curr:
            if curr[0] == key:
                return True
            curr = curr[1]
        return False

    @staticmethod
    def extract(text):
        return re.findall(r"[a-zA-Z]+", text.lower())

    def check(self, vocab_lines, text_lines):
        vocabulary = HashTable()
        for word in vocab_lines:
            vocabulary.add(word.strip())

        text_words = HashTable()
        for line in text_lines:
            for word in self.extract(line):
                text_words.add(word)
        words = True

        for bucket in text_words.table:
            curr = bucket
            while curr:
                if not vocabulary.cont(curr[0]):
                    words = False
                    break
                curr = curr[1]
        used = True

        for bucket in vocabulary.table:
            curr = bucket
            while curr:
                if not text_words.cont(curr[0]):
                    used = False
                    break
                curr = curr[1]

        if words and used:
            return "Everything is going to be OK."
        elif not words:
            return "Some words from the text are unknown."
        else:
            return "The usage of the vocabulary is not perfect."

vocab = [sys.stdin.readline().strip() for _ in range(n)]
text = [sys.stdin.readline().strip() for _ in range(m)]
print(HashTable().check(vocab, text))