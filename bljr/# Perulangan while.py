# Perulangan while
jumlah_langkah=0
while (jumlah_langkah < 10):
    print("saya sudah berjalan sebanyak", jumlah_langkah, "langkah")
    jumlah_langkah += 1 #jaraknya 1, kalai misalnya +=2 brrti jaraknya 2
    
# perulangan for
for angka in [1, 2, 3, 4, 5]:
    print("Ini perulangan ke -", angka)
 
for makanan in ["Rawon", "Soto Lamongan", "Gudeg", "Babi Kecap", "Rendang", "Nasi Padang", "Bakso"]:
    print(makanan, "Merupakan makanan khas nusantara")

for abjad in ["a","b","c","d","e"]:
    print(abjad, "ini adalah alphabet")
    
# praktikum while perulangan
number=1
while number <= 10:
    print(number)
    number=number+1
print("program selesai")

# ngitung rata rata pakai perulangan

print("Menghitung rata rata nilai dengan perulangan")

banyaknyadata = 5
i = 0

print("")

jumlah = 0

while i <5:
    nilai= int(input("Masukkan data ke-%d: " % (i+1)))
    i = i +1
    jumlah = jumlah + nilai
    rata_rata = jumlah/banyaknyadata
print("\nRata-rata = %0.2f" % rata_rata)

# tugas praktikum
from math import factorial
# no1
nilai = int(input("Masukkan nilai : "))
factorial = 1

for i in range(1, nilai + 1):
    factorial*= i
print(f"{nilai}! = {factorial}")

# no2
bill=1
for bill in range(1,16):
    if bill %2 != 0:
        print(bill, end=" ,")
       
# bil=0
# for bil in[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
#     if bil %2!= 0:
#     print(bil, "Yang termasuk bilangan ganjil adalah")

