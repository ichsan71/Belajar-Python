# Belajar Loop

## while

count = 0

while count < 5:
    print("saya guanteng")
    count += 1
else:
    print("udeh udeh" + " Countnya sekarang : " + str(count))

print("="*30)

## For
orang = ['san', 'kusming', 'kusmang']

for nama in orang:
    print('nama namanya adalah : ' + nama)


## Percabangan

a = 1

while a < 5:
    b = 0
    while b < a:
        print("*", end="")
        b += 1
    print()
    a += 1    