def profile(nama,alamat,gender,umur,hobi):
    print("nama saya adalah", nama)
    print("alamat saya di", alamat)
    print("gender saya adalah",gender)
    print("umur saya",umur )
    print("hobi saya adalah", hobi)

profile("monica","depok","wanita","19 tahun","menonton film")

print("=========================================")

def cetak_nilai(nilai):
    if(nilai <=60):
        return("gagal")
    elif(nilai >=61 and nilai <=70):
        return("baik")
    elif(nilai >=71 and nilai <=80):
        return("sangat baik")
    elif(nilai >= 81 and nilai <=100):
        return("istemewa")
    else:
        return("nilai tidak ada")

cetak_nilai(90)
cetak_nilai(65)
print("=============================")

def bilangan_ganjil(ganjil):

    for i in range(ganjil):
        if (i %2 !=0):
            print(i,end=' ')
bilangan_ganjil(100)
