import BlockCipher as bc
import random as rd


class CBC:

    def __init__(self, plainText, key):
        self.plainText = plainText
        self.key = key

    def generate_subPlains64(self, plainText):
        i = 0
        subPlains_64 = []
        if len(plainText) < 64:
            return subPlains_64.append(plainText.zfill(64))

        while True:
            subPlains_64.append(plainText[i:i+64])
            i += 64
            if i >= len(plainText):
                return subPlains_64
            if i+64 >= len(plainText):
                subPlains_64.append(plainText[i:len(plainText)].zfill(64))
                return subPlains_64

    def cellOps(self):

        rand = rd.randint(1, 1000000000)
        bin_rand = bin(rand)[2:]
        bin_rand = bin_rand.zfill(64)

        bc.xor(self.plainText, self.bin_rand)


c = CBC(bc.plainText, bc.key)
s = c.generate_subPlains64(bc.key)
print(s)
