class Mobil():
     def __init__(self, jendela, pintu, mesin):
          self.__jendela = jendela
          self.__pintu = pintu
          self.__mesin = mesin
spek = Mobil("hitam", "disel", "mam" )
print("spek :", spek.jendela)