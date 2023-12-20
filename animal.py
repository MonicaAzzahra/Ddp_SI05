class animal:
    def __init__(self,nama,makanan,hidup,berkembangBiak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangBiak = berkembangBiak

    def cetak(self):
        print("nama hewan ini adalah",self.nama)
        print("makanan kesukaan hewan ini adalah",self.makanan)
        print("hewan ini hidup di",self.hidup)
        print("hewan ini berkembang biak dengan cara",self.berkembangBiak)

class badak(animal):
    def __init__(self,nama,makanan,hidup,berkembangBiak,bergerak,bernapas):
        super().__init__(nama,makanan,hidup,berkembangBiak)
        self.bergerak = bergerak
        self.bernapas = bernapas

    def cetak(self):
        super().cetak()
        print("hewan ini bergerak dengan menggunakan",self.bergerak)
        print("hewan ini bernapas dengan menggunakan",self.bernapas)

class ikan(animal):
    def __init__(self,nama,makanan,hidup,berkembangBiak,bergerak,bernapas):
        super().__init__(nama,makanan,hidup,berkembangBiak)
        self.bergerak = bergerak
        self.bernapas = bernapas

    def tampil(self):
        super().cetak()
        print("hewan ini bergerak dengan menggunakan",self.bergerak)
        print("hewan ini bernapas dengan menggunakan",self.bernapas)

class ular(animal):
    def __init__(self, nama,makanan,hidup,berkembangBiak,bergerak,bernapas):
        super().__init__(nama,makanan,hidup,berkembangBiak)
        self.bergerak = bergerak
        self.bernapas = bernapas

    def hasil(self):
        super().cetak()
        print("hewan ini bergerak dengan menggunakan",self.bergerak)
        print("hewan ini bernapas dengan menggunakan",self.bernapas)

x = badak("badak","rumput","darat","melahirkan","kaki","paru-paru")
x.cetak()

print()

y = ikan("ikan","pelet","air","bertelur","sirip","insang")
y.tampil()

print()

z = ular("ular","daging - dagingan", "amphibi","bertelur","melata","paru-paru")
z.hasil()
