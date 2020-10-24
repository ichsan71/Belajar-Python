# memnbuat pertidaksamaan

# ------0+++++5------8+++++++11------

# input User
inputUser = float(input("Masukan Nilai :"))

# kurang dari 5
iskurangdari5 = inputUser < 5

# lebih dari 0
islebihdari0 = inputUser > 0

# lebih dari 8
islebihdari8 = inputUser > 8

# kurang dari 11
iskurangdari11 = inputUser < 11

gabung = iskurangdari5 and islebihdari0 or iskurangdari11 and islebihdari8


print("Angka yang anda masukan :", gabung)


# ++++++0------5++++++8------11++++++

# input User
inputUser = float(input("Masukan Nilai :"))

# lebih dari 5
islebihdari5 = inputUser > 5

# kurang dari 0
iskurangdari0 = inputUser < 0

# lebih dari 11
islebihdari11 = inputUser > 11

# kurang dari 8
iskurangdari8 = inputUser < 8

gabung = iskurangdari0 or islebihdari5 or iskurangdari8 or islebihdari11


print("Angka yang anda masukan :", gabung)



