# Variabel adalah tempat menyimpan data

# drop / assignment nilai
x = 5
y = 7

# pemangilan pertama
print("Nilai x = ", x)
print("Nilai y = ", y)
print("Nilai x+y = ", x+y)

# penamaan
nilai_z = 3  # dengan mengunakan underscore
juta10 = 10000000  # angka tdk boleh didepan
nilaiZ = 3  # bisa juga mengunakan huruf besar tapi disambung

# pemangilan kedua
print("Nilai y = ", y)
y = 6
print("Nilai y = ", y)

# assignment indirect
b = y
print("Nilai b = ", b)


# tipe data satuan yang tidak ber koma (integer)
data_integer = 1

print("data : ", data_integer)
print("-bertipe : ", type(data_integer))


# tipe data : angka dengan koma (float)
data_float = 1.5

print("data : ", data_float)
print("- bertipe : ", type(data_float))


# tipe data : Kumpulan karakter (string)
data_string = "ucup"

print("data : ", data_string)
print("- bertipe : ", type(data_string))

# tipe data : Biner true/false (Boolean)
data_bool = True

print("data : ", data_bool)
print("- bertipe : ", type(data_bool))

## Tipe data Khusus

# Bilangan Kompleks
data_complex = complex(5,6)

print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

# Tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(15.6)

print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))


## Casting
# merubah satu tipe ke tipe lain
# tipe data = int, float, str, bool

# INTEGER
print("=======INTEGER========")
data_int = 7;
print("data = ", data_int)
print("-bertipe =", type(data_int))

data_float = float(data_int)
print("data = ", data_float)
print("-bertipe =", type(data_float))

data_str = str(data_int)
print("data = ", data_str)
print("-bertipe =", type(data_str))

data_bool = bool(data_int) # akan flase jika nilai int = 0
print("data = ", data_bool)
print("-bertipe =", type(data_bool))

# Float
print("=======FLOAT========")
data_float = 5.3;
print("data = ", data_float)
print("-bertipe =", type(data_float))

data_int = int(data_float) #akan dibulatkan kebawah
print("data = ", data_int)
print("-bertipe =", type(data_int))

data_str = str(data_float)
print("data = ", data_str)
print("-bertipe =", type(data_str))

data_bool = bool(data_float) # akan flase jika nilai int = 0
print("data = ", data_bool)
print("-bertipe =", type(data_bool))

# Boolean
print("=======Bolean========")
data_bool = False;
print("data = ", data_bool)
print("-bertipe =", type(data_bool))

data_int = int(data_bool) #akan dibulatkan kebawah
print("data = ", data_int)
print("-bertipe =", type(data_int))

data_str = str(data_bool)
print("data = ", data_str)
print("-bertipe =", type(data_str))

data_float = float(data_bool) # akan flase jika nilai int = 0
print("data = ", data_float)
print("-bertipe =", type(data_float))

# String
print("=======STRING========")
data_str = "10"
print("data = ", data_str)
print("-bertipe =", type(data_str))

data_int = int(data_str) # string harus angka 
print("data = ", data_int)
print("-bertipe =", type(data_int))


data_float = float(data_str) # string harus angka
print("data = ", data_float)
print("-bertipe =", type(data_float))

data_bool = bool(data_str) # false jika strig kosong
print("data = ", data_bool)
print("-bertipe =", type(data_bool))


## Input User

data = input("Masukan data:")

print("data = ", data, type(data) )

#Integer
number = float(input("Masukan angka:"))

print("data = ", number, "type =" ,type(number) )

#Boolean
biner = bool(int(input("Masukan nilai bool:")))

print("data = ", biner, ",type =" ,type(biner) )


