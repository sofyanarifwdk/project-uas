# Buat dictionary untuk menyimpan inputan data mahasiswa
data_mahasiswa = {}


# Buat fungsi tambah_data
def tambah_data():
    print('======<  Create Data Mahasiswa  >======')
    print('=======================================')


# Buat fungsi hapus_data
def hapus_data():
    print('||======< Hapus Data Mahasiswa >======||')
    print('||====================================||')
    nama = input('Masukkan Nama Mahasiswa\t\t:')
    if nama in data_mahasiswa.keys():
        del data_mahasiswa[nama]
        print('\n||=====< Data mahasiswa berhasil dihapus >=====||')
    else:
        print('\nData {0} Tidak Ditemukan'.format(nama))


# Buat fungsi ubah_data
def ubah_data():
    print('\nMengubah Data Mahasiswa')
    print('=======================')
    nama = input('Masukkan Nama Mahasiswa\t\t: ')
    if nama in data_mahasiswa.keys():
        nim = int(input('Masukkan NIM Baru Mahasiswa\t: '))
        tugas = int(input('Masukkan Nilai Tugas Terbaru\t: '))
        uts = int(input('Masukkan Nilai UTS Terbaru\t: '))
        uas = int(input('Masukkan Nilai UAS Terbaru\t: '))
        hasil = (tugas*0.3) + (uts*0.35) + (uas*0.35)
        data_mahasiswa[nama] = nim, tugas, uts, uas, hasil
        print('\n||=====< Data Mahasiswa berhasil diubah >=====||')
    else:
        print('\nData {0} Tidak Ditemukan'.format(nama))


# Buat fungsi cari_data
def cari_data():
    print('=======<  Cari Data Mahasiswa  >=======')
    print('=======================================')
