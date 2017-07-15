from min import kurang
from x import kali
from div import bagi

def program_main(): #define the main program
    print("PROGRAM KALKULATOR \"SEDERHANA\"")
    print("------------------")


    print("Pilih angka 1-4 untuk melakukan operasi ")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    pil = int(input("Ketik angkanya :"))
    #operasi
    if pil == 1:
        from plus import jumlah
    elif pil == 2:
        kurang()
    elif pil == 3:
        kali()
    elif pil == 4:
        bagi()
    else:
        print("masukan salah !")

    #pengulangan
    loop = str(input("mau diulangi?"))
    if loop == "ya":
        program_main()
    elif loop == 1:
        program_main()
    elif loop == "yes":
        program_main()
    elif loop == "y":
        program_main()
    else:
        exit()

program_main()
