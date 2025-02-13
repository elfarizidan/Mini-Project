welcome_massage = "Welcome to Adheey's Page!"
belajar_posisi = "coding"

print("*******************************")
print(f"** {welcome_massage} **")
print("*******************************")

nama_user = input("masukan nama kamu: ")

bentuk_emot = "-_-"
emot = [bentuk_emot] * 3

emot[0] = ">.<"
print(emot)
print(f"maka:{belajar_posisi}")

print(f'''
      halo {nama_user}! Mau ngapain hari ini?
      coding / tidur / scroll tiktok
      ''')

pilihan_user = input("ketik di sini jawaban kamu: ")

confirm_answer = input(f"apakah kamu yakin dengan jawbanmu? {pilihan_user}? [iya/tidak]: ")

if confirm_answer == "tidak": 
    print("program dihentikan")
    exit()
elif confirm_answer == "iya": 
    if pilihan_user == belajar_posisi:
        print("yuk mulai belajar!")
    else:
        print("yakin ga mau belajar? ga mau jadi pns emangnya?")
else:
    print("berakhir...")
    exit()
