plainText = '1101001110110010101010101110101110011001101010011111000101110101'
key = '11010011101100101010101011101011100110011010100111110001011101001100101010100101011011101011110011010100101011011100101011011010'


def expand_to_64bit(binary_str):
    if len(binary_str) > 64:
        raise ValueError("Binary string must be less than or equal to 64 bits")
    return binary_str.zfill(64)


def generate_subkeys(key):
    pass


def generate_subPlains(plain):
    p1 = plain[0:16]
    p1 = plain[16:32]
    p1 = plain[32:48]
    p1 = plain[48:64]
    return [p1, p2, p3, p4]


def cipherBlock(key, plain):
    subKey_arr = generate_subkeys(key)
    plain_arr = generate_subPlains(plain)
    j = 0
    for i in range(8):
        plain_arr = roundOps(plain_arr, subKey_arr[j:j+6])
        j = j+6
    c1, c2, c3, c4 = lastRoundOps(plain_arr, subKey_arr[48:52])
    return c1+c2+c3+c4


def addModular(bin_str1, bin_str2):
    return str((int(bin_str1, 2)+int(bin_str2, 2)) % (2**16))


def multiplyModular(bin_str1, bin_str2):
    return str((int(bin_str1, 2)*int(bin_str2, 2)) % (2**16+1))


def xor(bin_str1, bin_str2):
    return ''.join(str(int(a) ^ int(b)) for a, b in zip(bin_str1, bin_str2))


def roundOps(plain_arr, subKey_arr):
    p1, p2, p3, p4 = plain_arr
    k1, k2, k3, k4, k5, k6 = subKey_arr

    s1 = multiplyModular(p1, k1)
    s2 = addModular(p2, k2)
    s3 = addModular(p3, k3)
    s4 = addModular(p4, k4)
    s5 = xor(s1, s3)
    s5 = xor(s2, s4)

    s7 = multiplyModular(s5, k5)
    s8 = addModular(s6, s7)
    s9 = multiplyModular(s8, k6)
    s10 = addModular(s7, s9)
    s11 = xor(s1, s9)
    s12 = xor(s3, s9)
    s13 = xor(s2, s10)
    s14 = xor(s4, s10)
    return [s11, s12, s13, s14]


def lastRoundOps(plain_arr, subKey_arr):
    r1, r2, r3, r4 = plain_arr
    k1, k2, k3, k4 = subKey_arr
    s1 = multiplyModular(r1, k1)
    s2 = addModular(r2, k2)
    s3 = addModular(r3, k3)
    s4 = multiplyModular(r4, k4)
    return [s1, s2, s3, s4]
