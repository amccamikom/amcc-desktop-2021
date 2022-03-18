# Make class

"""Membuat analogi class member AMCC yang memiliki atribut nama dan nim"""


class member_amcc():

    def nama(self):
        nama = None
        return nama

    def nim(self):
        nim = None
        return nim

    def cetak(self):
        print("Nama saya", self.nama, "dan NIM saya adalah", self.nim)


x = member_amcc()
x.nama = "Denisa Ramadhani"
x.nim = "19.12.1160"
x.cetak()
