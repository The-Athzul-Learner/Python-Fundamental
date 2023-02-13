# Exercise Date & Time Library
import datetime as dt
hari_ini = dt.date.today()
print(hari_ini)


tanggal = dt.date(2005,10,10)
print(tanggal)

# Latihan
print("Silahkan masukan tanggal, bulan, dan tahun lahir anda!")
tanggal = int(input("Tanggal : "))
bulan = int(input("Bulan : "))
tahun = int(input("Tahun : ") )
tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")


hari_ini = dt.date.today()
print(f"Hari ini tanggal : {hari_ini}")
umur_hari = hari_ini -tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365 )//30
print(f"Hari nya adalah :{tanggal_lahir:%A}")
print(f"Umur anda adalah :{umur_tahun} tahun {umur_bulan_sisa} bulan")
