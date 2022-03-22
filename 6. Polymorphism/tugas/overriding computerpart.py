#Eusebia Nawang Ari
#5210411195

# Overriding

class ComputerPart:
    def __init__(self, pabrikan, nama, jenis, harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
    
class Processor(ComputerPart):
    def __init__(self, pabrikan, nama, harga, jumlah_core, speed):
        super().__init__(pabrikan, nama, 'processor', harga)
        self.jumlah_core = jumlah_core
        self.speed = speed
    
    # method overloading
    def fungsi(self):
        print(f'{self.jenis} merupakan komponen untuk menjalankan proses komputasi dikomputer Anda')

class RandomAccessMemory(ComputerPart):
    def __init__(self, pabrikan, nama, harga, kapasitas):
        super().__init__(pabrikan, nama, 'RAM', harga)
        self.kapasitas = kapasitas
    
    # method overloading
    def fungsi(self):
        print(f'{self.jenis} merupakan memori sementara dikomputer Anda')

class HardDiskSATA(ComputerPart):
    def __init__(self, pabrikan, nama, harga, kapasitas, rpm):
        super().__init__(pabrikan, nama, 'HarddiskSATA', harga)
        self.kapasitas = kapasitas
        self.rpm = rpm

    # method overloading
    def fungsi(self):
        print(f'{self.jenis} sebagai tempat menyimpan file secara permanent dikomputer')

p = Processor('AMD Ryzen 5 5500u', 'Core i7',16000000, 4,'8 Ghz')
m = RandomAccessMemory('Sandisk', 'DD4 4 SECEPAT KILAT', 1000000,'128 GB')
hdd = HardDiskSATA('WD', 'WD Green', 1400000, '1200 GB',7200)

parts = [p,m,hdd]
for part in parts:
    print('{} {} pabrikan {}'. format(part.jenis, part.nama, part.pabrikan))
    part.fungsi()
    print("")