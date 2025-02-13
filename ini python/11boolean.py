# operasi logika atau boolean

# not, or, and, xor

# NOT
print ('----NOT----')
a = True
c = not a
print('data a =',a)
print('----------------NOT')
print('data c =',c)

# OR (jika salah satu true, maka hasilnya true)
print ('\n----OR----')
a = True
b = True
c = a or b
print(a,'OR',b,'=',c)

a = True
b = False
c = a or b
print(a,'OR',b,'=',c)

a = False
b = True
c = a or b
print(a,'OR',b,'=',c)

a = False
b = False
c = a or b
print(a,'OR',b,'=',c)

# AND (keduanya harus true)
print ('\n----AND----')
a = True
b = True
c = a and b
print(a,'AND',b,'=',c)

a = True
b = False
c = a and b
print(a,'AND',b,'=',c)

a = False
b = True
c = a and b
print(a,'AND',b,'=',c)

a = False
b = False
c = a and b
print(a,'AND',b,'=',c)

# XOR (akan true jika salah satu true, )
print ('\n----XOR----')
a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)

a = True
b = False
c = a ^ b
print(a,'XOR',b,'=',c)

a = False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)

a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
