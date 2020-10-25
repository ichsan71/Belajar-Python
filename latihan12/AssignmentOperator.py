# operasi yang dapat dilakukan daengan penyingkatan
# operasi ditambah dengan assignment

a = 5 # adalah assignment
print("nilai a :", a)

# Assigntment (+=)
a += 1 # sama dengan a = a + 1
print("nilai a += 1, nilai a menjadi :",a)

# Assigntment (-=)
a -= 2 # sama dengan a = a - 2
print("nilai a -= 2, nilai a menjadi :",a)

# Assigntment (*=)
a *= 3 # sama dengan a = a * 3
print("nilai a *= 3, nilai a menjadi :",a)

# Assigntment (/=)
a /= 3 # sama dengan a = a / 3
print("nilai a /= 3, nilai a menjadi :",a)

b = 10
print("\nnilai b :", b)

# Assigntment (%=)
b %= 3 # sama dengan b = b % 3
print("nilai b %= 3, nilai b menjadi :",b)

b = 10
print("\nnilai b :", b)

# Assigntment (//=)
b //= 3 # sama dengan b = b // 3
print("nilai b //= 3, nilai b menjadi :",b)

a = 5 
print("\nnilai a :", a)

# Assigntment (**=)
a **= 2 # sama dengan a = a ** 2
print("nilai a **= 2, nilai a menjadi :",a)

print("=============BITWISE=============")
## operasi bit wise
c = True
print("Nilai c =",c)

# Assigntment OR (|)
c |= False # sama dengan c = c | False
print("nilai c |= False, nilai c menjadi :",c)

c = False
print("Nilai c =",c)
c |= False # sama dengan c = c | False
print("nilai c |= False, nilai c menjadi :",c)

# Assigntment AND (&)
c = True
print("\nNilai c =",c)

c &= False # sama dengan c = c & False
print("nilai c &= False, nilai c menjadi :",c)

c = True
print("Nilai c =",c)
c &= True # sama dengan c = c & True
print("nilai c &= True, nilai c menjadi :",c)

# Assigntment XOR (^)
c = True
print("\nNilai c =",c)

c ^= False # sama dengan c = c ^ False
print("nilai c ^= False, nilai c menjadi :",c)

c = True
print("Nilai c =",c)
c ^= True # sama dengan c = c ^ True
print("nilai c ^= True, nilai c menjadi :",c)

# geser geser
d = 0b0100
print("\nnilai d =",format(d,'04b'))

# shift right (>>=)
d >>= 2 # sama dengan d = d >> 2
print("nilai d >>= 2, nilai d menjadi :",format(d,'04b'))


# shift left (<<=)
d <<= 1 # sama dengan d = d << 1
print("nilai d <<= 1, nilai d menjadi :",format(d,'04b'))
