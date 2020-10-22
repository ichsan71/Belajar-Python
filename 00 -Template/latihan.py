# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

fahrenheit = float(input("masukan suhu fahrenheitnya :"))
print("suhunya adalah :", fahrenheit, "fahrenheit")

# Celcius
celcius = 5 / 9 * (fahrenheit - 32)
print("suhunya adalah : ", celcius, "celcius" )

# reamur 
reamur = 4 / 9 * (fahrenheit - 32)
print("suhunya adalah : ", reamur, "reamur")

# kelvin 
kelvin = (5 / 9 * (fahrenheit - 32)) + 273
print("suhunya adalah : ", kelvin, "kelvin")

####
kelvin = float(input("masukan suhu kelvinnya :"))
print("suhunya adalah :", kelvin, "kelvin")

fahrenheit = (9 / 5 * (kelvin - 273)) + 32
print("suhunya adalah : ", fahrenheit, "fahrenheit")

