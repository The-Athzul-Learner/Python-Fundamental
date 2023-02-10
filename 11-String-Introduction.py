data = "Ini adalah string"
print(data)
print(type(data))
##1.Cara membuat string
"""
1. dengan menggunakan single quote '....'
2. dengan menggunakan double quote
"""
data = 'menggunakan single quote'
data2 = "menggunakan double quote"
print(data)
print(data2)

print('"Hallo, apa kabar?"')
print("'Hallo, apa kabar'")

##2. Menggunakan tanda \

# Membuat tanda ' menjadi string
print('mari sholat jum\'at')

# backslash
print("C:\\user\\Ucup")

# tab
print("Ucup\totong, jauhan")
print("Ucup\t\t\totong, semakin jauhan")

# backspace
print("Ucup \botong, deketan")

# newline
print("baris pertama.\nbaris kedua.")

##3. String literal atau raw

#hati-hati
print('C:\new folder') #akan salah pathnya
"""Solusinya menggunakan raw string"""
print(r'C:new\t\n\new folder')

#Multiline literal string
print("""
Nama  : Athallah 
Kelas : 3 SMP """)

# multiline literal string dan raw
print(r'''
Nama : Athallah Nuzul H
Kelas : 3 SD
Website : www.akuganteng123.com ''')