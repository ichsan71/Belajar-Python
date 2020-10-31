print(
"""
Masukan Kode barang!
1. Pakaian [PK01]
2. Tas [TS02]
3. Sepatu [SP03]
4. Aksesoris [AK04]
""")
print("="*30)

# Input User
kode_barang = str(input("Masukan Kode Barang : "))
kode_barang = kode_barang.upper()

jmlh_barang = int(input("Masukan Jumlah Barang : "))

# Pengkondisian
if kode_barang == 'PK01':
    kode_barang = 'PAKAIAN'
    harga_barang = 75000

elif kode_barang == 'TS02':
     kode_barang = 'TAS'
     harga_barang = 65000

elif kode_barang == 'SP03':
     kode_barang = 'SEPATU'
     harga_barang = 157000

elif kode_barang == 'AK04':
     kode_barang = 'AKSESORIS'
     harga_barang = 45000

else:
    print("Anda memasukan Pilihan yang salah")

if kode_barang == 'PAKAIAN' or kode_barang == 'AKSESORIS':
    diskon = 0.1*harga_barang
else:
    diskon = 0


# Output
print("Harga Barang         : " + str(harga_barang))
print("Jumlah Barang        : " + str(jmlh_barang))
print("Diskon               : " + str(diskon))
Hdiskon = harga_barang - diskon
print("Harga Setelah Diskon : " + str(Hdiskon) +'/barang')
Total_harga = jmlh_barang * Hdiskon
print("Total Harga          : " + str(Total_harga))

