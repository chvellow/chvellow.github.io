# perulangan part 2

buah = ["apel", "strawbery", "cherry"]
kata = ["merah", "besar", "enak"]

for x in buah:
    for y in kata:
        print(x,y)

i = 2
while(i < 30):
    j = 2
    while(j <= (i/j)):
        if not(i%j): break
        j = j + 1
    if (j > i/j) : print (i, " adalah bilangan prima")
    i = i+1
print("Good bye")

#Deklarasi variabel
var_nilai = 0
var_i = 1
#Perulangan WHILE
while (var_nilai < 10) :
    print("Perulangan pertama Ke ",var_nilai)
    while(var_i < 3) :
        print(" Perulangan ke ", var_nilai,", ",var_i)
        var_i +=1
    #diluar perulangan var_i
    var_i = 1
    var_nilai +=1
# diluar_perulangan var_nilai
print("var_nilai = ",int(var_nilai)," = 10. Bernilai False")

var_nilai = 0
var_i = 1
#Perulangan FOR
for var_nilai in range (0,10) :
    print("Perulangan pertama Ke ",var_nilai)
    while(var_i < 3) :
        print(" Perulangan ke ", var_nilai,", ",var_i)
        var_i +=1
    #diluar perulangan var_i
    var_i = 1
# diluar_perulangan var_nilai
print("var_nilai = ",int(var_nilai)+1," = 10. Bernilai False")

# segitiga kiri
string = ""
bar = 1
x = 8
while bar <= x:
    kol = bar
    while kol > 0:
        string = string + " * "
        kol = kol - 1
    string = string + "\n"
    bar = bar + 1
print(string)
# segitiga kanan
print("sgitiga kanan")
string = ""
bar = x
x = int(input("Masukkan angka : "))

while bar <= x:
    kol = bar
    while kol > 0:
        string = string + "  "
        kol = kol - 1
    kanan = 1
    while kanan < (x - (bar-1)):
        string = string + " * "
        kanan = kanan + 1
    string = string + "\n"
    bar = bar - 1
    
print(string)

# segitiga
string = ""
x = int(input("Masukkan angka :"))
bar = x
# Looping Baris
while bar >= 0:
# Looping Kolom Spasi Kosong
    kol = bar
    while kol > 0:
        string = string + " "
        kol = kol - 1
    # Looping Kolom Bintang Sisi Kiri
    kiri = 1
    while kiri < (x - (bar - 1)):
        string = string + " * "
        kiri = kiri + 1
# Looping Kolom Bintang Sisi Kanan
    kanan = 1
    while kanan < kiri - 1:
        string = string + " * "
        kanan = kanan + 1
    string = string + "\n\n"
    bar = bar - 1
print(string)

# sgitiga
tinggi = int(input("Masukkan tinggi bintang segitiga "))
for i in range(tinggi, 0,-1):
    print("" * (tinggi-i) + "*" * i)
    
    
# sgtg

string =" "
baris = 1

x = int(input("Masukkan tinggi bintang segitiga :  "))
print("\n")

while baris <= x:
    kolom = baris
    while kolom >1:
        string = string + "  "
        kolom = kolom -1
    kiri = 0
    while kiri <= (x - baris):
        string = string + " * "
        kiri = kiri +1
    kanan = kiri
    while kanan > 1:
        string = string + " * "
        kanan = kanan -1
        
    string = string + "\n\n"
    baris = baris + 1
print(string)