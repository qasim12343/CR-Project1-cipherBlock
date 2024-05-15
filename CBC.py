import BlockCipher as bc
import random as rd


class CBC_CTR:

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

    def cbc_cellOps(self, IV, subPlain, key):
        s1 = bc.xor(subPlain, IV)
        s2 = bc.cipherBlock(key, s1)
        return s2

    def CBC(self):

        cipherBlocks = []
        subPlains_64 = self.generate_subPlains64(self.plainText)
        rand = rd.randint(1, 1000000000)
        bin_rand = bin(rand)[2:]
        bin_rand = bin_rand.zfill(64)
        c = self.cbc_cellOps(bin_rand, subPlains_64[0], key)
        cipherBlocks.append(c)
        for i in range(1, len(subPlains_64)):
            c = self.cbc_cellOps(c, subPlains_64[i], key)
            cipherBlocks.append(c)
        return cipherBlocks

    def ctr_cellOps(self, key, counter, subPlain):

        s1 = bc.cipherBlock(key, counter)
        s2 = bc.xor(subPlain, s1)
        return s2

    def CTR(self):
        cipherBlocks = []
        subPlains_64 = self.generate_subPlains64(self.plainText)

        for i in range(0, len(subPlains_64)):
            counter = bin(i)[2:].zfill(64)
            c = self.ctr_cellOps(self.key, counter, subPlains_64[i])
            cipherBlocks.append(c)
        return cipherBlocks


plainText = '110100111011001010101010111010111001100110101001111100010111010101'
key = '11010011101100101010101011101011100110011010100111110001011101001100101010100101011011101011110011010100101011011100101011011010'

c = CBC_CTR(plainText, key)
c1 = c.CBC()
c2 = c.CTR()
print(c1)
print(c2)
