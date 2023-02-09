print("TEMPERATURE CONVERSION PPROGRAM")

celcius = float(input("Masukan suhu dalam celcius: "))
print("Suhu dalam celcius adalah", celcius)
#Celcius to Reamur
reamur = (4/5)*celcius
print("Suhu dalam reamur adalah ", reamur)

#Celcius to Fahrenheit
fahrenheit = (9/5)*celcius+32
print("Suhu dalam fahrenheit adalah ", fahrenheit)

#Celcius to kelvin
kelvin= celcius+273
print("Suhu dalam kelvin adalah ", kelvin)

##Homework
#Converse Fahrenheit to kelvin amd otherwise
fahrenheit = float(input("Masukan suhu dalam fahrenheit: "))
fahrenheit_kelvin = 5/9*(fahrenheit-32)+273
print("Suhu dalam kelvin adalah ", fahrenheit_kelvin)

kelvin = float(input("Masukan suhu dalam kelvin: "))
kelvin_fahrenheit = 9/5*(kelvin-273)+32
print("Suhu dalam fahrenheit adalah ", kelvin_fahrenheit)


