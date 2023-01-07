# import data_mahasiswa di folder model yang terdapat daftar_nilai
from model.daftar_nilai import data_mahasiswa


# Buat fungsi input_data
def input_data():
    no = 0
    jawab = "y"
    while (jawab == "y"):
        nama = input('\nMasukkan Nama Mahasiswa\t\t: ')
        nim = int(input('Masukkan NIM Mahasiswa\t\t: '))
        tugas = int(input('Masukkan Nilai Tugas\t\t: '))
        uts = int(input('Masukkan Nilai UTS\t\t: '))
        uas = int(input('Masukkan Nilai UAS\t\t: '))
        hasil = (tugas*0.3) + (uts*0.35) + (uas*0.35)
        data_mahasiswa[nama] = nim, tugas, uts, uas, hasil
        jawab = input("Tambah data (y/t)?\t\t: ")
        no += 1
