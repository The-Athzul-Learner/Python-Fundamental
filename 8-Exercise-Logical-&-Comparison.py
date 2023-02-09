##Practice Logic and Comparation

#Membuat gabungan area rentang dari angka
rentang=float(input("Masukan angka yang lebih dari 3 dan kurang dari 10: "))
#++++++3
lebihDari3 = (rentang > 3)
print("Lebih dari 3 =", lebihDari3)
#------10
kurangDari10 = (rentang < 10)
print("Kurang dari 10 =", kurangDari10)
#rentang >3 and <10
hasil = lebihDari3 and kurangDari10
print("angka yang anda masukan =", hasil )


rentang=float(input("Masukan angka yang kurang dari 3 atau lebih dari 10: "))
#++++++3
kurangDari3 = (rentang < 3)
print("kurang dari 3 =", kurangDari3)
#------10
lebihDari10 = (rentang > 10)
print("lebih dari 10 =", lebihDari10)
#rentang >3 and <10
hasil = kurangDari3 or lebihDari10
print("angka yang anda masukan =", hasil )