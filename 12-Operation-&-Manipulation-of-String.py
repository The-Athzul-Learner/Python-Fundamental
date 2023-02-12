##Operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_pertama = "ucup"
nama_tengah = "D"
nama_akhir = "Fame"

nama_lengkap = nama_pertama+" "+nama_tengah+" "+nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari", nama_lengkap, str(panjang))

# 3. Operator untuk string
# Mengecek apakah ada komponen char atau string di string
d = 'd'
status = d in nama_lengkap
print(d + "ada di " + nama_lengkap + " = "+ str(status))

# mengulang string
print("wk"*10)

#Indexing
print("Index ke-0 : " + nama_lengkap[0])
print("Index ke-1 : " + nama_lengkap[1])
print("Index ke-(-1) : " + nama_lengkap[-1]) #jika negatif index dimulai dari belakang mulai dari -1
print("Index ke-6 : " + nama_lengkap[6])
print("Index ke-(3:7) : " + nama_lengkap[3:8]) #mengambil komponen dengan range, tidak akan mengambil angka terakhir
print("Index ke-(0,2,4,6,8,10) : " + nama_lengkap[0:11:2]) #jika negatif index dimulai dari belakang mulai dari -1

# Item paling kecil
print("paling kecil : " + min(nama_lengkap))
# Item paling besar
print("paling kecil : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

###4. Operator dalam bentuk method
#menghitung jumlah komponen
data = "otong surotong paraptong"
jumlah =data.count("o")
print("jumlah o pada", data, "=", str(jumlah))
##merubah case dari string
#merubah semua ke upper case
salam = "bro!"
print("normal = ", salam)
salam = salam.upper()
print("upper =", salam)
#merubah semua ke lower case
alay = "aKu Kece AbieZZZZZZZZ"
print("normal = ", alay)
alay = alay.lower()
print("lower = ", alay)

##Pengecekan dengan isX method

#Pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() #hasilnya bool
print(salam+ " is lower = "+ str(apakah_lower))
apakah_upper = salam.isupper() #hasilnya bool
print(salam+ " is upper = "+ str(apakah_upper))

#isalpha() -->Untuk mengecek semuanya huruf
#isalnum()  -->Huruf dan angka
#isdecimal() --> angka saja
#isspace() -->spasi, tab, new line \n
#istitle() --> semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Okay"
cek_judul = judul.istitle()
print(judul, "is title =", cek_judul)

##Mengecek komponen startswith( endswith( <-- keren
cek_start = "Sangjangnim Oppa".startswith("sangjangnim")
print("start =", cek_start)
cek_end = "Sangjangnim Oppak".endswith(("Oppak"))
print("end =", cek_end)

##Penggabungan Komponen