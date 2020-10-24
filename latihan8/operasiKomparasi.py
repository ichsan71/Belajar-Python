# Operasi Komparasi, Comparation value
# Setiap hasil dari operasi komparasi adalah boolean

# >,<,>=,<=,==,!=,is,is not

x = 2
y = 4

print("---------- Lebih dari > ----------")
# lebih dari >
hasil = x > y
print(x,'>',y,'=', hasil)

hasil = y > x
print(y,'>',x,'=', hasil)

hasil = x > x
print(x,'>',x,'=', hasil)


print("---------- Kurang dari < ----------")
# Kurang dari <
hasil = x < y
print(x,'<',y,'=', hasil)

hasil = y < x
print(y,'<',x,'=', hasil)

hasil = x < x
print(x,'<',x,'=', hasil)

print("---------- Lebih dari atau sama dengan >= ----------")
# Lebih dari atau sama dengan >=
hasil = x >= y
print(x,'>=',y,'=', hasil)

hasil = y >= x
print(y,'>=',x,'=', hasil)

hasil = x >= x
print(x,'>=',x,'=', hasil)

print("---------- Kurang dari atau sama dengan <= ----------")
# Kurang dari atau sama dengan <=
hasil = x <= y
print(x,'<=',y,'=', hasil)

hasil = y <= x
print(y,'<=',x,'=', hasil)

hasil = x <= x
print(x,'<=',x,'=', hasil)

print("---------- sama dengan == ----------")
# sama dengan =
hasil = x == y
print(x,'==',y,'=', hasil)

hasil = y == x
print(y,'==',x,'=', hasil)

hasil = x == x
print(x,'==',x,'=', hasil)

print("---------- Tidak sama dengan != ----------")
# Tidak sama dengan !=
hasil = x != y
print(x,'!=',y,'=', hasil)

hasil = y != x
print(y,'!=',x,'=', hasil)

hasil = x != x
print(x,'!=',x,'=', hasil)

print("---------- is ----------")
# is hanya bisa di komparasikan dengan variabel atau object identity
hasil = x is y
print(x,'is',y,'=', hasil)

hasil = x is y
print(x,'is',y,'=', hasil)

hasil = x is x
print(x,'is',x,'=', hasil)

print("---------- is not ----------")
# is not hanya bisa di komparasikan dengan variabel atau object identity
hasil = x is not y
print(x,'is not',y,'=', hasil)

hasil = x is not y
print(x,'is not',y,'=', hasil)

hasil = x is not x
print(x,'is not',x,'=', hasil)


