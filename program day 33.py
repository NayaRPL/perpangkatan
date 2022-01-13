print("menuntukan cara apa yang dipakai untuk menentukan hasil perpakatan")
print("cara pertama : operator perpangkatan")
bilangan=int(input("masukkan bilangan:"))
pangkat=int(input("masukkan pangkat:"))
hasil=bilangan**pangkat
print("hasil perpangkatan:",hasil)

print("cara ke dua: fungsi rekursif")
def hasil_perpangkat(bilangan,pangkat):
    if pangkat > 1:
        return bilangan*hasil_perpangkat(bilangan,pangkat-1)
    return bilangan
hasi=hasil_perpangkat(5,4)
print("hasil perpangkatan:",hasil)

print("cara ke tiga: perulangan")
hasil=5
pangkatan=4
for i in range(pangkatan-1):
  hasil *= 5
print(hasil)
