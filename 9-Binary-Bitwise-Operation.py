##Operator Bitwise, Operasi binary
"""Bitwise = Operasi masing masing bit
#Operator Bitwise : AND (&), OR (|), XOR(^), NOT(~)
untuk integer =1 -> 00000001 (bit memiliki index 0-7 yang dimulai dari kanan yang menjadi pangkat dari 2(biner))
latihan :
1. 00001000 int = ?
   int = 8
2. 00001001
   int = 2^3+2^0 = 9
"""

a = 8
b = 5
# bitwise OR (|)
c = a|b
print("============OR=============")
print('nilai :',a , ', binary :', format(a,'08b'))
print('nilai :', b, ', binary : ', format(b,'08b'))
print("=============================(|)")
print('nilai :', c, ', binary : ', format(c,'08b'))

# bitwise AND (&)
c = a&b
print("============OR=============")
print('nilai :',a , ', binary :', format(a,'08b'))
print('nilai :', b, ', binary : ', format(b,'08b'))
print("=============================(&)")
print('nilai :', c, ', binary : ', format(c,'08b'))

# bitwise XOR (^)
c = a^b
print("============OR=============")
print('nilai :',a , ', binary :', format(a,'08b'))
print('nilai :', b, ', binary : ', format(b,'08b'))
print("=============================(^)")
print('nilai :', c, ', binary : ', format(c,'08b'))

# bitwise NOT (~)
c = ~a
print("============OR=============")
print('nilai :',a , ', binary :', format(a,'08b'))
print('nilai :', b, ', binary : ', format(b,'08b'))
print("=============================(~)")
print('nilai :', c, ', binary : ', format(c,'08b'))
print("================FLIP=============(^)")
d = 0b00000101
e = 0b11111111
print('nilai :', e^d, ', binary : ', format(e^d,'08b'))

# Shifting Right (>>)
c = a >> 1
print("============OR=============")
print('nilai :',a , ', binary :', format(a,'08b'))
print('nilai :', b, ', binary : ', format(b,'08b'))
print("=============================(^)")
print('nilai :', c, ', binary : ', format(c,'08b'))

# Shifting Left (<<)
c = a << 1
print("============OR=============")
print('nilai :',a , ', binary :', format(a,'08b'))
print('nilai :', b, ', binary : ', format(b,'08b'))
print("=============================(^)")
print('nilai :', c, ', binary : ', format(c,'08b'))
