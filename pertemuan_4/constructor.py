# Make class w/ constructor

"""Membuat analogi class member AMCC yang memiliki atribut nama dan nim dengan
konsep constructor"""


class member_amcc():

    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def cetak(self):
        print("Nama saya", self.nama, "dan NIM saya adalah", self.nim)


x = member_amcc("Denisa Ramadhani", "19.12.1160")
x.cetak()
