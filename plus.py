def jumlah():
    a = int(input("masukkan angka pertama :"))
    b = int(input("masukkan angka kedua : "))
    c = penjumlahan(a, b)
    print("Hasil penjumlahan dari", a, "+", b, "adalah ",c)
def penjumlahan(angka1, angka2):
    return angka1 + angka2

jumlah()