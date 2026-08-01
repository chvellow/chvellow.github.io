x = int(input("Masukkan angka : "))
y = int(input("Masukkan angka : "))

print("x berisi angka",x, "decimal atau", bin(x), "biner")
print("y berisi angka",y, "decimal atau", bin(y), "biner")

kalimat = "stiki"
print('kalimat yang diinputkan adalah : ', kalimat)
print('\'i\' in kalimat :', 'i' in kalimat)
print('\'2\' not in kalimat :', '2' not in kalimat)
print('\'d\' not in kalimat :', 'd' not in kalimat)

a = 5
b = 9
c = 6
print('a is b : ', a is b)
print('a is c : ', a is c)
print('a is not c : ', a is not c)


print("Menghitung luas segitiga")
alas = input("Masukkan alas segitiga : ")
tinggi = input("Masukkan tinggi segitiga : ")
luas = (float(alas) * float(tinggi))/2
print("Luas segitiga adalah : ", luas)

print("")
print("Menghitung luas lingkaran")
diameterA = float (input("Masukkan diameter A :"))
diameterB = float (input("Masukkan diameter B :"))
jariA = diameterA//2
jariB = diameterB//2
phi = 3.143

luasA = 0.5 * phi * jariA* jariA
luasB = 2 * 0.5 * phi * jariB*  jariB
luas_total = luasA - luasB
print("Luas A : ",luasA)
print("Luas B : ",luasB)
print("Luas total : ",luas_total)






