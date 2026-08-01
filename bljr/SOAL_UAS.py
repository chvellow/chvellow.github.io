print("Soal nomor 1")
#buat fungsi input angka dulu
def input_angka(nilai):
    while True: #akan diulang sampai benar menginputkan 
        try: #return tuk balikin angka trs keluar dri perulangann 
            return int(input(nilai)) #minta data dari pengguna dan ubah iinput mnjadi angka
        except ValueError:
            print("Input tidak valid. Mohon masukkan angka.") #kalau nilainya eror akan dialihkan kesini 
# gaji = input_angka("Masukkan gaji anda: ")
# jam_kerja = input_angka("Masukkan jam kerja anda: ")

# tunjangan = gaji * 10 / 100
# gaji_lembur = 30000


# if gaji and jam_kerja<0:
#     print("Masukkan dengan benar")
# else: 
#     if jam_kerja > 40:
#         hasil_lembur = (jam_kerja - 40) * gaji_lembur
#         total_gaji = gaji + tunjangan + hasil_lembur
#         print("Selamat anda mendapat upah lembur sebanyak: ", hasil_lembur)
#     else:
#         total_gaji = gaji + tunjangan
#         print("Tetap semangat untuk lembur!")
#     print("Anda mendapatkan tunjangan sebanyak: ", tunjangan)
#     print("Total Gaji yang anda dapatkan adalah: ", total_gaji)


print("Soal nomor 2")

penghasilan_orang_tua = input_angka("Masukkan penghasilan orang tua anda : ")
meteran_kwh = input_angka("Masukkan jumlah KWH meteran pada rumah anda : ")
nilai = str(input("Masukkan nilai anda [A/B/C/D/E] : ")).strip().upper()

if penghasilan_orang_tua<=3000000 :
    if meteran_kwh<= 900:
        if nilai == "A" :
            print("Anda berhasil dan berhak mendapatkan beasiswa")
        elif nilai == "B":
            print("Anda berhasil dan berhak mendapatkan beasiswa")
        elif nilai == "C":
            print("Mohon maaf anda belum bisa mendapatkan beasiswa")
        else :
            print("Mohon maaf anda belum bisa mendapatkan beasiswa")
    else: 
        print("Mohon maaf anda belum bisa mendapatkan beasiswa")
else:
    print("Mohon maaf anda belum bisa mendapatkan beasiswa")

print("Soal nomor 3")
jumlah_bintang = input_angka("masukkan tinggi segitiga bintang : ")
for i in range(1, jumlah_bintang +1):
    print((jumlah_bintang - i+1) * "#")
    # 10 jumlah bintang
    # 1 1 1 1 1 1 1 1 1 1
    # 1 1 1 1 1 1 1 1 1
    # 1 1 1 1 1 1 1 1 
    # dst
    
# 5-1+1 = 5
# 5-2 +1 = 4
# 5-3 + 1 =3 
            
print("Soal nomor 4")
mahasiswa =["Yellownita", "Ayres", "Adrian", "Yandex", "Jehes"]
jurusan = ["DKV", "IT", "BD", "FK", "FEB"]

print(list(zip(mahasiswa , jurusan)))
