# Inheritance concept

"""Membuat analogi class member AMCC yang berasal dari
divisi yang berbeda-beda tapi memiliki atribut yang sama yaitu nama dan nim"""


class member_amcc():

    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def cetak(self):
        print("Nama saya", self.nama, "dan NIM saya adalah", self.nim)


class desktop(member_amcc):

    def __init__(self, nama, nim):
        super().__init__(nama, nim)
        self.divisi = "Desktop Programming"
        self.bahasa = "Python"

    def cetak(self):
        super().cetak()
        print("Divisi saya adalah", self.divisi,
              "dengan basis bahasa", self.bahasa)


x = desktop("Denisa Ramadhani", "19.12.1160")
x.cetak()
