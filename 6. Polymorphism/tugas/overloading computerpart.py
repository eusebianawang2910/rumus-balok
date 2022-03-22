#Eusebia Nawang Ari
#5210411195

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
    def kecepatanProcessor(self, speed):
        if(speed >= 3):
            print("kecepatan Processor cepat")
        else :
            print("kecepatan Processor normal")

class RandomAccessMemory(ComputerPart):
    def __init__(self, pabrikan, nama, harga, kapasitas):
        super().__init__(pabrikan, nama, 'RAM', harga)
        self.kapasitas = kapasitas


class HardDiskSATA(ComputerPart):
    def __init__(self, pabrikan, nama, harga, kapasitas, rpm):
        super().__init__(pabrikan, nama, 'SATA', harga)
        self.kapasitas = kapasitas
        self.rpm = rpm

p = Processor('AMD Ryzen 5 5500u', 'Core i7',16000000, 4,'8 Ghz')
m = RandomAccessMemory('Sandisk', 'DD4 4 SECEPAT KILAT', 1000000,'128 GB')
hdd = HardDiskSATA('WD', 'WD Green', 1400000, '1200 GB',7200)

parts = [p,m,hdd]
for part in parts:
    print('{} {} pabrikan {}'. format(part.jenis, part.nama, part.pabrikan))

p.kecepatanProcessor(6.5)