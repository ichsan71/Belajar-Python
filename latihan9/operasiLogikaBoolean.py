#Operator Logika/Boolean

#not, or, and, xor

print('====NOT====')
x = True
z = not x

print('data x =', x)
print('----------------------NOT')
print('data z =', z)

#OR jika salah satu true maka hasilnya true
print('====OR====')
x = False
y = False
z = x or y
print(x,'or',y,'=',z)

x = True
y = True
z = x or y
print(x,'or',y,'  =',z)

x = True
y = False
z = x or y
print(x,'or',y,' =',z)

x = False
y = True
z = x or y
print(x,'or',y,' =',z)

#AND Kedua nya harus true untuk mendapatkan hasil true
print('====AND====')
x = False
y = False
z = x and y
print(x,'and',y,'=',z)

x = True
y = True
z = x and y
print(x,'and',y,'  =',z)

x = True
y = False
z = x and y
print(x,'and',y,' =',z)

x = False
y = True
z = x and y
print(x,'and',y,' =',z)

#XOR akan true jika salah satu true
print('====XOR====')
x = False
y = False
z = x ^ y
print(x,'^',y,'=',z)

x = True
y = True
z = x ^ y
print(x,'^',y,'  =',z)

x = True
y = False
z = x ^ y
print(x,'^',y,' =',z)

x = False
y = True
z = x ^ y
print(x,'^',y,' =',z)