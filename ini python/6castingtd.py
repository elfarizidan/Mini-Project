# merubah dari satu tipe ke tipe yang lain
# tipe data= int, float, string, boolean

#integer
print("-------------Integer-------------")
data_int = 0;
print("data: ", data_int, "- type: ", type(data_int))

data_float = float(data_int)
print("data: ", data_float, "- type: ", type(data_float))
data_str = str(data_int)
print("data: ", data_str, "- type: ", type(data_str))
data_bool = bool(data_int) # akan false jika nilai int = 0
print("data: ", data_bool, "- type: ", type(data_bool))

# float
print("\n -------------Float-------------")
data_float = 9.7;
print("data: ", data_float, "- type: ", type(data_float))

data_int = int(data_float) # akan dibulatkan ke bawah
print("data: ", data_int, "- type: ", type(data_int))
data_str = str(data_float)
print("data: ", data_str, "- type: ", type(data_str))
data_bool = bool(data_float) # akan false jika nilai float = 0
print("data: ", data_bool, "- type: ", type(data_bool))

# boolean
print("\n -------------Boolean-------------")
data_bool = False;
print("data: ", data_bool, "- type: ", type(data_bool))

data_int = int(data_bool) # akan dibulatkan ke bawah
print("data: ", data_int, "- type: ", type(data_int))
data_str = str(data_bool)
print("data: ", data_str, "- type: ", type(data_str))
data_float = float(data_bool) # akan false jika nilai float = 0
print("data: ", data_float, "- type: ", type(data_float))

# string
print("\n -------------String-------------")
data_str = "13";
print("data: ", data_str, "- type: ", type(data_str))

data_int = int(data_str) # string harus angka
print("data: ", data_int, "- type: ", type(data_int))
data_float = float(data_str) # string harus angka
print("data: ", data_float, "- type: ", type(data_float))
data_bool = bool(data_str) # false jika string kosong
print("data: ", data_bool, "- type: ", type(data_bool))