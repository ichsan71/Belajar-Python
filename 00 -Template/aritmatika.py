## Operasi Aritmatika
x = 10
y = 3

# operasi tambah +
hasil = x + y
print(x, '+',  y, '=', hasil)

# operasi kurang -
hasil = x - y
print(x, '-',  y, '=', hasil)

# operasi kali *
hasil = x * y
print(x, '*',  y, '=', hasil, type(hasil))

# operasi bagi /
hasil = x / y
print(x, '/',  y, '=', hasil, type(hasil))

# operasi eksponen (berpangkat) **
hasil = x ** y
print(x, '**',  y, '=', hasil, type(hasil))

# operasi modulus (sisa bagi) %
hasil = x % y
print(x, '%',  y, '=', hasil, type(hasil))

# operasi floor division (pembulatan hasil bagi) //
hasil = x // y
print(x, '//',  y, '=', hasil, type(hasil))

# prioritas operasi, operational precendence
'''
    1. ()
    2. exponen **
    3. perkalian dkk *  /  %  //
    4. penjumlahan dkk +  -
'''

a = 2
b = 3
c = 4

hasil = a + b * c - a / b ** c % a // b
print(a, '+', b, '*', c, '-', a, '/', b, '**', c, '%', a, '//', b, "adalah =", hasil)

