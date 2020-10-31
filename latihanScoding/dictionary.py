# Belajar Dictionary {}
# Dictionary key:value 
# memanggil index menggunakan string dan panggil dengan key nya!

data = {'name' :'san',
        'age'  : 18,
        'Hobby':'fly'
        }

print("umur saya adalah " + str(data['age']))
print("="*30)

# menambahkan isi dictionary
data['dream'] = 'programmer'
print(data)
print("dream saya adalah " + data['dream'])
print("="*30)

# mengubah/edit isi dictionary 
data['name'] = 'Koesmang'
print(data['name'])
print("="*30)

# menghapus isi dictionary
del data['name']
print(data)
print("="*30)

# menggunakan for in dengan dictionary
for key, value in data.items():
    print(str(key) + ' : ' +str(value))

