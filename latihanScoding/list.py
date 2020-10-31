# Belajar List []
# list index (angka perhitungan dimulai dari 0)
# -1 akan mulai dari paling kanan index

orang = ['san', 'Kusming', 'kusmang']
umur  = [10,20,50,100,80]
mixed = [1,'text', 'editor',2.5]

print(orang[0])

# menambahkan isi list
orang.append('urusei')
print(orang)

# mengganti isi dari List
orang[1] = "Koesmung"
print(orang)

# menghapus isi dari List
del umur[-2]
print(umur)