# Belajar Dictionary {}
# Dictionary key:value 
# memanggil index menggunakan string dan panggil dengan key nya!

data = {'name' :'san',
        'age'  : 18,
        'Hobby':'fly'
        }

print("umur saya adalah" + str(data['age']))

print("====Add Dictionary====")
# menambahkan isi dictionary
data['dream'] = 'programmer'
print(data)
print("dream saya adalah " + data['dream'])


print("====Edit Dictionary====")
# mengubah/edit isi dictionary 
data['name'] = 'Koesmang'
print(data['name'])

print("====Delete Dictionary====")
# menghapus isi dictionary
del data['name']
print(data)

print("====Using Dictionary with for in====")
# menggunakan for in dengan dictionary
for key, value in data.items():
    print(str(key) + ' : ' +str(value))


print("====Nested Dictionary====")
# Nested dictionary
data2 = {1:{'name':'Koesmang', 'age':'10', 'hobby':'nyolong'},
         2:{'name':'Koesming', 'age':'9', 'hobby':'manjat'},
         3:{'name':'Koesmung', 'age':'8', 'hobby':'nyakar'}}

print(data2)
print()
print(data2[3])
print()
print(data2[1]['hobby'])

print("====Nested Dictionary with For in====")
# Nested dictionary with For in
for key, value in data2.items():
    print("\nKeynya: ",key)

    for key2 in value:
        print(key2 + ' : ', value[key2])
