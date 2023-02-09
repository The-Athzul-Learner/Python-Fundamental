##Operasi Logika atau Boolean

#Operator : not, and, or, xor

#NOT
print("=====NOT====")
x = True
y = not x
print('data x =', x)
print("------NOT")
print('data y =', y)

#AND
print("=====AND====")
x = True
y = True
z = x and y
print(x, 'AND', y, '  =', z)
x = True
y = False
z = x and y
print(x, 'AND', y, ' =', z)
x = False
y = True
z = x and y
print(x, 'AND', y, ' =', z)
x = False
y = False
z = x and y
print(x, 'AND', y, '=', z)

#OR
print("=====OR====")
x = True
y = True
z = x or y
print(x, 'OR', y, '  =', z)
x = True
y = False
z = x or y
print(x, 'OR', y, ' =', z)
x = False
y = True
z = x or y
print(x, 'OR', y, ' =', z)
x = False
y = False
z = x or y
print(x, 'OR', y, '=', z)

#XOR
print("=====XOR====")
x = True
y = True
z = x ^ y
print(x, 'XOR', y, '=', z)
x = True
y = False
z = x ^ y
print(x, 'XOR', y, '=', z)
x = False
y = True
z = x ^ y
print(x, 'XOR', y, '=', z)
x = False
y = False
z = x ^ y
print(x, 'XOR', y, '=', z)