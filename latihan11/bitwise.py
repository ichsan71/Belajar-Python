# bitwise adalah operator binary

x = 9
y = 5

# bitwise OR (|)
z = x | y
print('\n=======OR=======')
print('Nilai :',x,' , binary :',format(x,'08b'))
print('Nilai :',y,' , binary :',format(y,'08b'))
print('-----------------------------------(|)')
print('Nilai :',z,' , binary :',format(z,'08b'))

# bitwise AND (&)
z = x & y
print('\n=======AND=======')
print('Nilai :',x,' , binary :',format(x,'08b'))
print('Nilai :',y,' , binary :',format(y,'08b'))
print('-----------------------------------(&)')
print('Nilai :',z,' , binary :',format(z,'08b'))

# bitwise XOR (^)
z = x ^ y
print('\n=======XOR=======')
print('Nilai :',x,' , binary :',format(x,'08b'))
print('Nilai :',y,' , binary :',format(y,'08b'))
print('-----------------------------------(^)')
print('Nilai :',z,' , binary :',format(z,'08b'))

# bitwise NOT (~)
z = ~x
print('\n=======NOT=======')
print('Nilai :',x,' , binary :',format(x,'08b'))
print('-----------------------------------(~)')
print('Nilai :',z,' , binary :',format(z,'08b'))
print('-----------------------------------(^)')
a = 0b0000001001
b = 0b1111111111
print('Nilai :',a^b,' , binary :',format(a^b,'08b'))

# shifting

# shift right (>>)
z = x >> 1
print('\n=======>>=======')
print('Nilai :',x,' , binary :',format(x,'08b'))
print('-----------------------------------(>>)')
print('Nilai :',z,' , binary :',format(z,'08b'))

# shift left (<<)
z = x << 1
print('\n=======<<=======')
print('Nilai :',x,' , binary :',format(x,'08b'))
print('-----------------------------------(<<)')
print('Nilai :',z,' , binary :',format(z,'08b'))

