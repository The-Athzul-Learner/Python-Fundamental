##Operator assignment adalah operasi yang dapat dilakukan dengan penyingkatan
# Operasi ditmabah dengan assignment

a = 5 #ini adalah assignment
print('nilai =', a)

##Operator Assignment Aritmatika
print("=========ARITMATIKA=======")
a+=1 #sama dengan a=a+1
print("a+=1 nilai a menjadi", a)

a-=1 #sama dengan a=a-1
print("a-=1 nilai a menjadi", a)

a*=2 #sama dengan a=a*1
print("a*=2 nilai a menjadi", a)

a/=1 #sama dengan a=a/1
print("a/=1 nilai a menjadi", a)

a**=3 #sama dengan a=a**1
print("a**=3 nilai a menjadi", a)

a//=2 #sama dengan a=a//1
print("a//=2 nilai a menjadi", a)

a%=5 #sama dengan a=a%1
print("a%=5 nilai a menjadi", a)

## Operator Assignment Bitwise
print('===========BITWISE===========')
#OR
print('======OR')
c = True
print('nilai c =', c)
c |= False
print("c|=False nilai c menjadi", c)
c = True
print('nilai c =', c)
c |= True
print("c|=True nilai c menjadi", c)
#AND
print('======AND')
c = True
print('nilai c =', c)
c &= False  #c = c & False
print("c&=False nilai c menjadi", c)
c = True
print('nilai c =', c)
c &= True
print("c&=True nilai c menjadi", c)
#XOR
print('======XOR')
c = True
print('nilai c =', c)
c ^= False
print("c^=False nilai c menjadi", c)
c = True
print('nilai c =', c)
c ^= True
print("c^=True nilai c menjadi", c)
#Shifting
print('======>>')
d=0b0100
print('nilai d :', format(d,'04b'))
d>>=2
print('d>>=2 :', format(d,'04b'))
d<<=1
print('d>>=2 :', format(d,'04b'))