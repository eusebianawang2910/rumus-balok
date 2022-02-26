class Buku:
    def __init__(self, judul, pengarang, tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit


buku1 = Buku('Tenggelamnya Kapal Van Der Wijck', 'Hamka', 1938)
buku2 = Buku('Pendidikan Masyarakat', 'Paulo Freire', 2003)
buku3 = Buku('Pendidikan Karakter', 'Bagus Mustakim', 2011)
buku4 = Buku('Koala Kumal','Raditya Dika',2015)



data_buku = [buku1, buku2, buku3, buku4]

print('Daftar Buku')
for i in data_buku:
    print(
        f'Buku {i.judul} karangan {i.pengarang} pertama kali diterbitkan tahun {i.tahun_terbit}')
