# operasi Aritmathic

x = 10
y = 3

# Operasi tambah +
hasil = x + y
print(x,'+',y,'=',hasil)

# Operasi kurang -
hasil = x - y
print(x,'-',y,'=',hasil)

# Operasi kali *
hasil = x * y
print(x,'*',y,'=',hasil)

# Operasi bagi /
hasil = x / y
print(x,'/',y,'=',hasil)

# Operasi eksponen (pangkat) **
hasil = x ** y
print(x,'pangkat',y,'=',hasil)

# Operasi sisa bagi (mod/modulus) %
hasil = x % y
print(x,'%',y,'=',hasil)

# Operasi floor division (div) //
hasil = x // y
print(x,'//',y,'=',hasil)

# Prioritas operasi, operational precedence
# 1. Kurung ()
# 2. Eksponen **
# 3. kali,bagi,modulus(%),floorDiv(//)
# 4. tambah, kurang + -
a = 2
b = 3
c = 4

hasil = a ** b * c + a / b - b % c // a
print(a,'**',b,'*',c,'+',a,'/',b,'-',b,'%',c,'//',a,'=', hasil)