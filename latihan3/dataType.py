# macam2 tipe data pada Python

# tipe data: angka satuan/bil.bulat (integer)
data_integer =  11
print("data : ",data_integer)
print("-bertipe :", type(data_integer))

# tipe data: angka dengan koma/Pecahan (Float)
data_float = 1.5
print("data : ",data_float)
print("-bertipe :", type(data_float))

# tipe data: kumpulan karakter (String)
data_string = "Ichsan"
print("data : ",data_string)
print("-bertipe :", type(data_string))

# tipe data: biner true/false (Boolean)
data_boolean = True
print("data : ",data_boolean)
print("-bertipe :", type(data_boolean))

## tipe data khusus
# bilangan kompleks
data_complex = complex(5,6)
print("data : ",data_complex)
print("-bertipe :", type(data_complex))

# tipe data dari bahasa C
# tapi harus import librarynya duls
from ctypes import c_double

data_c_double = c_double(10.5)
print("data : ",data_c_double)
print("-bertipe :", type(data_c_double))


