print(""" 
Pilih Tujuan :
1. Jakarta
2. Yogyakarta
3. Surabaya""")
print("="*30)

tujuan = int(input("Masukan Pilihan Tujuan Anda [1,2,3] : "))

print(""" 
Pilih Kelas :
1. Ekonomi
2. Bisnis
3. Eksekutif""")
print("="*30)

kelas = int(input("Masukan Pilihan kelas Anda [1,2,3] : "))
banyak_tiket = int(input("Mau beli brp? : "))
print("="*30)
print("Hasil Perhitungan")
print("="*30)

if tujuan == 1:
    tujuan="Jakarta"
    
    if kelas == 1:
        kelas="Ekonomi"
        H_tiket=100000
    elif kelas == 2:
        kelas="Bisnis"
        H_tiket=400000
    elif kelas == 3:
        kelas="Eksekutif"
        H_tiket=700000
    else:
        print("Anda salah Memasukan Pilihan!")
elif tujuan == 2:
    tujuan="Yogyakarta"
    
    if kelas == 1:
        kelas="Ekonomi"
        H_tiket=200000
    elif kelas == 2:
        kelas="Bisnis"
        H_tiket=500000
    elif kelas == 3:
        kelas="Eksekutif"
        H_tiket=800000
    else:
        print("Anda salah Memasukan Pilihan!")
elif tujuan == 3:
    tujuan="Surabaya"
    
    if kelas == 1:
        kelas="Ekonomi"
        H_tiket=300000
    elif kelas == 2:
        kelas="Bisnis"
        H_tiket=600000
    elif kelas == 3:
        kelas="Eksekutif"
        H_tiket=900000
    else:
        print("Anda salah Memasukan Pilihan!")
else:
    print("anda salah memasukan pilihan")

if tujuan=="Yogyakarta" and kelas=="Ekonomi":
    diskon=0.1*H_tiket;
elif tujuan=="Surabaya" and kelas=="Eksekutif":
    diskon=0.1*H_tiket
else:
    diskon=0

print(str(banyak_tiket) + " x (Bandung-" + str(tujuan)+")" +" "+ str(kelas) )
print("Harga Tiket : " + str(H_tiket))
print("Diskon      : ",(diskon))
H_setelah_Diskon = H_tiket - diskon
print("Harga Setelah Diskon  : " + str(H_setelah_Diskon)+ "/Tiket")
total = banyak_tiket * H_setelah_Diskon
print("Total Bayar           : " + str(total))

