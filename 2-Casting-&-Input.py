##Casting dan Input
"""Input berguna untuk mengambil data dari user, sedangkan casting dapat membuat
tipe data yang dimasukan oleh user lebih spesifik"""

#Input
data = input("Siapa nama anda? ")
print("data :", data, "tipe :", type(data)) #data yang dimasukan pasti bertipe string

#Casting Input to Integer & Float
data = int(input("Berapa umur anda? "))
print("data :", data, "tipe :", type(data))

data = float(input("Berapa umur anda? "))
print("data :", data, "tipe :", type(data))

#Casting input to boolean
data = bool(int(input("Berapa umur anda? ")))
print("data :", data, "tipe :", type(data))