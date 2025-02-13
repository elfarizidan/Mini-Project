#fundamental logika

#typecasting
tanggal_lahir = "19"                # ini tipe data string
tanggal_lahir = int(tanggal_lahir)  # timpa nilai variabel sebelumnya untuk menampung tipe data baru
print(tanggal_lahir)                # 19 <- integer

#=======================================
#data list
kardus = ["semangka", "pisang", "nanas"]
print(len(kardus)) #isinya ada 3 data

kardus = ["semangka", "pisang", "nanas"]
print(kardus[0])
print(kardus[1])
print(kardus[2])

kardus = ["semangka", "pisang", "nanas"]
kardus.append("anggur")
kardus.append("jeruk")
print(kardus[4])
print(kardus[4 - 2])
# 4-2=2
# setara dgn print(kardus[2])
# maka hasilnya akan "nanas"

#=======================================

hobi = "fotografi, baca novel, tidur"
print(hobi)

hobbies = ["fotografi", "baca novel", "tidur"] 
            #   0,            1,         2
tmp_hobbies = hobbies
print(f"hobbies -> {hobbies}")
tmp_hobbies[1] = "nonton"
print(f"tmp_hobbies -> {tmp_hobbies}")