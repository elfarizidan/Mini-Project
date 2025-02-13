# operasi komparasi
#setiap hasil dari operas komparasi adalah boolean
# >, <, <=, >=, ==, !=, is, is not

a = 4
b = 2

# lebih besar dari >
print('-------- lebih besar dari (>) --------')
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = b > 2
print(b, '>', 2, '=', hasil)

# kurang dari <
print('\n-------- kurang dari (<) --------')
hasil = a < -3
print(a, '<', -3, '=', hasil)
hasil = b < 1
print(b, '<', 1, '=', hasil)
hasil = b < 0
print(b, '<', 0, '=', hasil)

# lebih besar dari sama dengan >=
print('\n-------- lebih besar dari (>=) --------')
hasil = a >= 3
print(a, '>=', 3, '=', hasil)
hasil = b >= 3
print(b, '>=', 3, '=', hasil)
hasil = b >= 2
print(b, '>=', 2, '=', hasil)

# kurang dari <=
print('\n-------- kurang dari (<=) --------')
hasil = a <= -3
print(a, '<=', -3, '=', hasil)
hasil = b <= 1
print(b, '<=', 1, '=', hasil)
hasil = b <= 0
print(b, '<=', 0, '=', hasil)

# sama dengan (==)
print('\n-------- sama dengan (==) --------')
hasil = a == 4
print(a, '==', 4, '=', hasil)
hasil = b == 1
print(b, '==', 1, '=', hasil)

# tidak sama dengan (!=)
print('\n-------- tidak sama dengan (!=) --------')
hasil = a != 4
print(a, '!=', 4, '=', hasil)
hasil = b != 1
print(b, '!=', 1, '=', hasil)

# 'is' sebagai komparasi objek identity
print('\n-------- objek identity (is) --------')
x = 5 # ini adalah assignment membuat objek
y = 5
print('nilai x =',x, ',id= ',hex(id(x)))
print('nilai y =',y, ',id= ',hex(id(y)))
hasil = x is y
print('x is 5 =',hasil)

# 'is' sebagai komparasi objek identity
print('\n-------- objek identity (is not) --------')
x = 5 # ini adalah assignment membuat objek
y = 5
print('nilai x =',x, ',id= ',hex(id(x)))
print('nilai y =',y, ',id= ',hex(id(y)))
hasil = x is not y
print('x is 5 =',hasil)

x = 5 # ini adalah assignment membuat objek
y = 7
print('\n=nilai x =',x, ',id= ',hex(id(x)))
print('nilai y =',y, ',id= ',hex(id(y)))
hasil = x is not y
print('x is 5 =',hasil)