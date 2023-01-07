# import data_mahasiswa di folder model yang terdapat daftar_nilai
from model.daftar_nilai import data_mahasiswa


# Buat fungsi cetak_daftar_nilai
def cetak_daftar_nilai():
    if data_mahasiswa.items():
        print('=============================== Daftar Nilai Mahasiswa ==================================')
        print('=========================================================================================')
        print('|  NO. |      NAMA     |      NIM      |    TUGAS   |   UTS   |   UAS   |  NILAI AKHIR  |')
        print('=========================================================================================')
        i = 0
        for x in data_mahasiswa.items():
            i += 1
            # metode string format (.format)
            print('| {6:4} | {0:13s} | {1:13} | {2:10d} |  {3:6d} | {4:7d} | {5:13.2f} | '
                  .format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
            print(
                '=========================================================================================')
    else:
        print('===================================== Daftar Nilai ===================================')
        print('======================================================================================')
        print('|  No  |      Nama     |      NIM      |   TUGAS  |   UTS   |   UAS   | Nilai Akhir  |')
        print('======================================================================================')
        print('|                                    Tidak Ada Data                                  |')
        print('======================================================================================')


# Buat fungsi cetak_hasil_pencarian
def cetak_hasil_pencarian():
    nama = input("Masukan Nama\t: ")
    # jika nama yang di ketik ada didalam dictionary cetak hasil. dan jika tidak ada maka akan else
    if nama in data_mahasiswa.keys():
        print("============================ Daftar Nilai ========================================")
        print("==================================================================================")
        print('|      Nama     |      NIM      |   TUGAS    |   UTS   |   UAS   | Nilai Akhir   |')
        print("==================================================================================")
        print("|{0:14s} | {1:13} | {2:10d} |  {3:6d} | {4:7d} | {5:13.2f} | "
              .format(nama, data_mahasiswa[nama][0], data_mahasiswa[nama][1], data_mahasiswa[nama][2], data_mahasiswa[nama][3], data_mahasiswa[nama][4]))
        print("==================================================================================")
    else:
        print("Datanya {0} tidak ada ".format(nama))
