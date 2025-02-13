# latihan konversi satuan suhu
# program konversi celcius ke satuan lain
print("\nProgram Konversi Temperatur\n")

celcius = float(input('Masukan suhu dalam celcius: '))
print("suhu adalah ", celcius, "Celcius")

# reamur
reamur = (4/5) * celcius #rumus
print("suhu dalam reamur adalah ", reamur, "reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32 #rumus
print("suhu dalam fahrenheit adalah ", fahrenheit, "fahrenheit")

# kelvin
kelvin = celcius + 273 #rumus
print("suhu dalam kelvin adalah ", kelvin, "kelvin")