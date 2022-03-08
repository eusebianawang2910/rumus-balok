class Buku:
    def __init__(self, judul, pengarang, tahun_terbit, harga):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.__harga = harga


buku1 = Buku('Tenggelamnya Kapal Van Der Wijck', 'Hamka', 1938, 20000)
buku2 = Buku('Pendidikan Masyarakat', 'Paulo Freire', 2003, 45000)
buku3 = Buku('Pendidikan Karakter', 'Bagus Mustakim', 2011, 60000)
buku4 = Buku('Koala Kumal','Raditya Dika',2015, 95000)



data_buku = [buku1, buku2, buku3, buku4]
print('Daftar Buku')
for i in data_buku:
    print(
        f'Buku {i.judul} karangan {i.pengarang} pertama kali diterbitkan tahun {i.tahun_terbit} dengan harga Rp. {i._Buku__harga}')
