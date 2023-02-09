##Data Types
"""In programming, data type is an important concept.
Variables can store data of different types, and different types can do different things."""

#Tipe data = angka (Integer)
data_integer = 11
print("Data integer = ",data_integer)
print("Tipe data :", type(data_integer))

#Tipe data = angka dengan koma (Float)
data_float = 0.5
print("Data Float = ", data_float)
print("Tipe data :", type(data_float))

#Tipe data = complex number (Complex)
data_complex = 7+8j
print("Data complex = ",data_complex)
print("Tipe data :", type(data_complex))

#Tipe data = Kumpulan character
data_string = "Atha"
print("Data string = ",data_string)
print("Tipe data :", type(data_string))

#Tipe data = biner true/false (boolean)
data_biner = True
print("Data biner = ",data_biner)
print("Tipe data :", type(data_biner))

print()

##Casting Data Type
"""Casting berguna untuk merubah tipe data ke tipe data yang lain"""

print("====STRING====")
data_str = "8"
print("Data =", data_str, "type=", type(data_str))

data_float = float(data_str) #String harus angka
data_int = int(data_str)     #String harus angka
data_biner = bool(data_str)  #String False jika kosong
print("Data =", data_int, "type=", type(data_int))
print("Data =", data_float, "type=", type(data_float))
print("Data =", data_biner, "type=", type(data_biner))

print("====FLOAT====")
data_float = 6.5
print("Data =", data_float, "type=", type(data_float))

data_str = str(data_float)
data_int = int(data_float)     #Pembulatan ke bawah
data_biner = bool(data_float)
print("Data =", data_str, "type=", type(data_str))
print("Data =", data_int, "type=", type(data_int))
print("Data =", data_biner, "type=", type(data_biner))

print("====INTEGER====")
data_int = 8
print("Data =", data_int, "type=", type(data_int))

data_str = str(data_int) #String harus angka
data_float = float(data_int)     #String harus angka
data_biner = bool(data_int)  #String False jika kosong
print("Data =", data_str, "type=", type(data_str))
print("Data =", data_float, "type=", type(data_float))
print("Data =", data_biner, "type=", type(data_biner))

print("====BOOLEAN====")
data_bool = True
print("Data =", data_bool, "type=", type(data_bool))

data_str = str(data_bool) #String harus angka
data_float = float(data_bool)     #String harus angka
data_int = int(data_bool)  #String False jika kosong
print("Data =", data_str, "type=", type(data_str))
print("Data =", data_float, "type=", type(data_float))
print("Data =", data_int, "type=", type(data_int))