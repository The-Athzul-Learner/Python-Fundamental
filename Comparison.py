##Operasi Komparasi
"""Operasi yang digunakan untuk membandingkan nilai. Setiap hasil dari operasi komparasi adalah
boolean."""
#Operator Komparasi : >, <, >=, <=, ==, !=, is, is not
x = 5
y = 6
#Lebih dari (>)
print("========= Lebih dari (>)")
hasil = x > 3
print(x, '>', 3, '=', hasil)
hasil = y > 3
print(y, '>', 3, '=', hasil)
hasil = x > 5
print(x, '>', 5, '=', hasil)

#Kurang dari (<)
print("========= kurang dari (<)")
hasil = x < 3
print(x, '<', 3, '=', hasil)
hasil = y < 8
print(y, '<', 8, '=', hasil)
hasil = x < 5
print(x, '<', 5, '=', hasil)

#Kurang dari sama dengan(<=)
print("========= kurang dari sama dengan (<=)")
hasil = x <= 3
print(x, '<=', 3, '=', hasil)
hasil = y <= 8
print(y, '<=', 8, '=', hasil)
hasil = x <= 5
print(x, '<=', 5, '=', hasil)

#Lebih dari sama dengan(<=)
print("========= lebih dari (>=)")
hasil = x >= 3
print(x, '>=', 3, '=', hasil)
hasil = y >= 8
print(y, '>=', 8, '=', hasil)
hasil = x >= 5
print(x, '>=', 5, '=', hasil)

#Sama dengan (==)
print("========= Sama dengan (==)")
hasil = x == 3
print(x, '==', 3, '=', hasil)
hasil = y == 8
print(y, '==', 8, '=', hasil)
hasil = x == 5
print(x, '==', 5, '=', hasil)

#Tidak sama dengan (!=)
print("========= Tidak sama dengan (!=)")
hasil = x != 3
print(x, '!=', 3, '=', hasil)
hasil = y != 8
print(y, '!=', 8, '=', hasil)
hasil = x != 5
print(x, '!=', 5, '=', hasil)

""">, <, >=, <=, ==, !=
Operasi berikut dapat bekerja untuk membandingkan  syntax literal yaitu data yang tidak akan tersimpan di 
memori seperti variabel. Fungsi "is dan is not" adalah untuk membandingkan objek/memori. """
x = 7 #7 adalah literal sedangkan x merupakan objek yang akan tersimpan dalam memori.
y = 7
z = 8
#'is' sebagai komparasi object identity
print("========= Is sebagai komparasi object (is)")
hasil = x is y
print(x, 'is', 7, '=', hasil)
hasil = x is z
print(x, 'is', z, '=', hasil)

#'is not' sebagai komparasi object identity
print("========= Is not sebagai komparasi object (is not)")
hasil = x is not y
print(x, 'is not', 7, '=', hasil)
hasil = x is not z
print(x, 'is not', z, '=', hasil)

