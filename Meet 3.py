("NAMA :Wisnu Tazridhu")
#("NIM  :25241005")
#("KELAS:PTI C")

while True:
    angka = int(input("Masukkan angka: "))
    if angka < 0:
        print("\033[91mHarus positif!\033[0m")

    
    else:
        print("Angka yang dimasukkan:", angka)
        break