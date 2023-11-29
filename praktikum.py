#no1
hasil_akhir = [
    {'nama': 'Reza', 'nilai': 70},
    {'nama': 'Ciut', 'nilai': 63},
    {'nama': 'Dian', 'nilai': 80},
    {'nama': 'Badu', 'nilai': 40}
]
siswa_lulus = [siswa['nama'] for siswa in hasil_akhir 
    if siswa['nilai'] > 65]
print(siswa_lulus)

#no2
buah_asli = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
buah_terbalik = []
for a in reversed(buah_asli):
    buah_terbalik.append(a)
print(buah_terbalik)

#no3
buah_asli = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
buah_terduplikasi = []
for a in buah_asli:
    buah_terduplikasi.append(a)
    buah_terduplikasi.append(a)
print(buah_terduplikasi)

#no4
nama = 'Nurul Fikri'
print(nama.replace('u','').replace('i',''))


