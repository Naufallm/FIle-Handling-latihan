# Import library yang dibutuhkan
import os

# Buat list untuk menyimpan data mahasiswa
data_mahasiswa = []

# Masukkan data mahasiswa ke dalam list
for nama, nim, semester in [
    ("Andi", 11119, 1),
    ("Bima", 11112, 1),
    ("Rahma", 11131, 3),
    ("Zeno", 11198, 9),
    ("Rahma", 11131, 3),
    ("Andi", 11119, 1),
]:
    data_mahasiswa.append((nama, nim, semester))

# Hapus data yang duplikat
data_mahasiswa = list(set(data_mahasiswa))

# Buat file txt
file = open("data_mahasiswa.txt", "w")

# Tulis data mahasiswa ke dalam file txt
for nama, nim, semester in data_mahasiswa:
    file.write(f"{nama} {nim} {semester}\n")

# Tutup file
file.close()
