#------0+++++5------8+++++11------
# lebih dari 0, kurang dari 5, 
# lebih dari 8, kurang dari 11

inputUser = float(input("Masukan angka: "))

# lebih dari 0 
isLebihDari = (inputUser > 0)
print("lebih dari 0 = ", isLebihDari)

# kurang dari 5
isKurangDari = (inputUser < 5)
print("kurang dari 5 = ", isKurangDari)

# lebih dari 8 
isLebihDari = (inputUser > 8)
print("lebih dari 8 = ", isLebihDari)

# kurang dari 11
isKurangDari = (inputUser < 11)
print("kurang dari 11 = ", isKurangDari)

isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan: ", isCorrect)
