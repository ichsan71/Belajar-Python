# operasi dan manipulasi string

### 1. menyambung string (concatenate)
nama_pertama = "kusmang"
nama_tengah = "kusming"
nama_akhir = "kusmung"

nama = nama_pertama +" "+ nama_tengah +" "+ nama_akhir

print(nama)

### 2. Menghitung panjang dari string
panjang = len(nama)
print("panjang dari nama adalah :" + str(panjang))

### 3. operator untuk string

# mengecek apakah ada komponen char atau string di dalam string

d = "k"
status = d in nama 
print(d + " ada di " + nama +" = "+ str(status))

d = "k"
status = d not in nama 
print(d + " ada di " + nama +" = "+ str(status))

# mengulang string
print("wk"*10)

# indexing
print("index ke-0 : " + nama[0])
print("index ke-6 : " + nama[6])
print("index ke-1 : " + nama[-1])
print("index ke-1 ampe 10 : " + nama[0:9])
print("index ke-[0,2,4,6,8,10] : " + nama[0:9:2])

# item paling kecil
print("paling Kecil :" + min(nama))

# item paling besar
print("paling besar :" + max(nama))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

### 4. operator dalam bentuk method

data = "kusming"
jumlah = data.count("i")
print('jumlah o pada data ' + data + " = " + str(jumlah))
