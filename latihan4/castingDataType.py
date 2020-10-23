# Kita belajar casting duls
# Casting adalah merubah dari satu tipe data ke tipe lain

print("------------------INTEGER----------------------------")
# INTEGER
data_int = 3
print("data =", data_int, ", type =", type(data_int))

# sekarang kita rubah duls
data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int) #akan false jika nilai = 0
print("data =", data_float, ", type =", type(data_float))
print("data =", data_str, ", type =", type(data_str))
print("data =", data_bool, ", type =", type(data_bool))

print("------------------FLOAT----------------------------")

# Float
data_float = 3.1
print("data =", data_float, ", type =", type(data_float))

# sekarang kita rubah duls
data_int = int(data_float)
data_str   = str(data_float)
data_bool  = bool(data_float) #akan false jika nilai = 0
print("data =", data_int, ", type =", type(data_int))
print("data =", data_str, ", type =", type(data_str))
print("data =", data_bool, ", type =", type(data_bool))


print("------------------STRING----------------------------")

# STRING
data_str = "3"
print("data =", data_str, ", type =", type(data_str))

# sekarang kita rubah duls
data_int   = int(data_str) #string harus angka
data_float = float(data_str)
data_bool  = bool(data_str) #string kosong = false
print("data =", data_int, ", type =", type(data_int))
print("data =", data_float, ", type =", type(data_float))
print("data =", data_bool, ", type =", type(data_bool))

print("------------------BOOLEAN----------------------------")

# BOOLEAN
data_bool = True 
print("data =", data_bool, ", type =", type(data_bool))

# sekarang kita rubah duls
data_int   = int(data_bool)
data_float = float(data_bool)
data_str   = str(data_bool) 
print("data =", data_int, ", type =", type(data_int))
print("data =", data_float, ", type =", type(data_float))
print("data =", data_str, ", type =", type(data_str))

