# latihan komparasi dan logika

# membuat gabungan area rentang dari angka
 
# +++++++3-----------10++++++++

inputUser = float(input("masukan angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10\n:"))

# +++++++3-----------------
# memriksa angka kurang dari 3
isKurangDari = (inputUser < 3)

# -------------------------10++++++
# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)

# menggabungkan
gabungan = isKurangDari or isLebihDari 

print("Angka yang anda masukan : ", gabungan)

# ---------3+++++++++10---------

inputUser = float(input("masukan angka yang bernilai\nlebih dari 3\ndan\nkurang dari 10\n:"))

# -----------3+++++++
# memriksa angka lebih dari 3
isLebihDari = (inputUser > 3)

# +++++++10----------
# memeriksa angka kurang dari 10
isKurangDari = (inputUser < 10)

# menggabungkan
gabungan = isLebihDari and isKurangDari 

print("Angka yang anda masukan : ", gabungan)



