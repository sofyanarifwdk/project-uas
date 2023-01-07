# Import semua fungsi yang terdapat pada daftar_nilai, input_nilai, view_nilai
from model.daftar_nilai import tambah_data, ubah_data, hapus_data, cari_data
from view.input_nilai import input_data
from view.view_nilai import cetak_daftar_nilai, cetak_hasil_pencarian

# while loop dan If statements
while True:
    print('\n======== PROGRAM INPUT DATA MAHASISWA ========')
    print('==============================================')
    print('\nPilih salah satu menu di bawah ini:')
    print('=====================================')
    print('\n1.(C)reate \n2.(R)ead \n3.(U)pdate \n4.(D)elete \n5.(S)earch \n6.(Q)uit')
    x = input('\nMasukkan Pilihan Menu anda\t: ')

    if x.lower() == "c":
        tambah_data()
        input_data()
    elif x.lower() == "r":
        cetak_daftar_nilai()
    elif x.lower() == "u":
        ubah_data()
    elif x.lower() == "d":
        hapus_data()
    elif x.lower() == "s":
        cari_data()
        cetak_hasil_pencarian()
    elif x.lower() == "q":
        print('Anda sudah keluar dari program')
        break
    else:
        print('Pilih menu yang tersedia di atas')
