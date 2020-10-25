data = 'ini adalah string'
print(data)
print(type(data))

### 1. cara membuat string

'''
    1. dengan menggunakan single quote '....'
    2. dengan menggunakan double quote "...."
'''

data = 'menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

print("'Halo vlog welkombek to ma ges'")
print('"Halo vlog welkombek to ma ges"')
print("ini adalah hari jum'at")

### 2. mnenggunakan tanda \

# membuat tanda ' menjadi string (\')
print('mari solat jum\'at')

# backslah (\\)
print("C:\\user\\kusming")

# tab (\t)
print("kusming\t\t\tkusmang, jauhan")

# newline (\n)
print("baris pertama.\nbaris kedua.")

### 3. String literal atau raw

# Raw string (r)
print(r'C:\new \t\t\tfolder')

# multiline literal string ("""....""")
print("""
Nama : kusmang
Kelas : paud
""")

# multiline literal string RAW 
print(r"""
C:\newfolder
dude
""")