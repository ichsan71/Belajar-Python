# operator dalam bentuk methods

## merubah case dari data string

# merubah semua ke upper case
salam = "bro!"
print("normal = " + salam)

salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case
alay = "KoEsMiNg"
print("normal = " + alay)

alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan isX method

# contoh pengecekan lower case dan upper case
salam = "sist"
apakah_lower = salam.islower() # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper()
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
# isalnum() <-- untuk mengecek huruf dan angka
# isdecimal() <-- untuk mengecek angka saja
# isspace() <-- untuk mengecek spasi, tab, newline \n
# istitle() <-- semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle()
print(judul + " is title = " + str(cek_judul))

## ngecdek komponen startswith() endswith() <-- Keren
cek_start = "Koesmang Kuesming".startswith("Koesmang")
print("start = " + str(cek_start) )

cek_with = "Koesmang Kuesming".endswith("Kuesming")
print("with = " + str(cek_with) )

## penggabungan komponen join () split()
pisah = ['aku','sayang','kamu']
gabung = 'gk'.join(pisah)
print(pisah)
print(gabung)


gabung = "akugksayanggkkamu"
print(gabung.split('gk'))

# alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,"-")
print("'"+tengah+"'")


