#Membuat Konversi binner ke decimal

#input User
n1 = int(input("Masukan Nilai Pertama :"))
n2 = int(input("Masukan Nilai kedua   :"))
n3 = int(input("Masukan Nilai ketiga  :"))
print("-----------------------------------------")

rumus = (n1 * (2 ** 2)) + (n2 * (2 ** 1)) + (n2 * (2 ** 0)) 

print(n1,n2,n3)
print("-----------------------------------------")

#output User
print('(',n1,'*',2,'pangkat',2,') + (',n2,'*',2,'pangkat',1,') + (',n2,'*',2,'pangkat',0,') = ', rumus, "dalam decimal")


