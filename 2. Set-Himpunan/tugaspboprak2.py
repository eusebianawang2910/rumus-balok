#EUSEBIA NAWANG ARI
#5210411195
#PRAKTIKUM PBO PRAKTIK

str1 = "aku cinta indonesia"
print(str1)

str2 = str1[:10]+'tanah airku'+str1[9:]
print(str2)

str3 = 'aku cinta tanah air ku indonesia'
str4 = str3[:9]+''+str3[22:]
print(str4)

kelas = 'Praktikum Pemrograman Berorientasi Objek'
up = kelas.upper()
lo = kelas.lower()
print(kelas)
print(up)
print(lo)

s = '     python     '
print(s.strip())
print(s.lstrip())
print(s.rstrip())

print(len(kelas))

jumlah = len(kelas)
print('panjang string adalah :',jumlah)

s1 = 'python '
s2 = 'programing'
print(s1+s2)

print(kelas.index('a'))
print(kelas)

kelas2 = kelas.replace('Praktikum','praktik')
print(kelas2)

a = 'satu'
b = 'dua'
c = 'tiga'
print('saya mempunyai %s mangga'%(b))

print(kelas.split())

# input1 = input('hari ini adalah : ')
# print(input1)

# data1 = input('angka 1 : ')
# data2 = input('angka 2 : ')
# data3 = int(data1)+int(data2)
# print(data1,' * ',data2,' = ',data3)

list1 = [1,2,3,4,5,6,7,8,9]
# print(list1)
# print(list1[5])
# print(list1[:3])
# print(len(list1))
# print(list1[10-3:])
# print(list1[2:9])
# print(list1[-10])
# print(list1[0])
# list1.append(10)
# print(list1)
# list1.insert(1,11)
# print(list1)

list2 = ['hello']
list1.extend(list2)
print(list1)

list1.extend('hai')
print(list1)

del list1[1]
print(list1)

list1.remove(5)
print(list1)

list1.pop()
print(list1)

a = [50,20,30,40]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
print(min(a))
print(max(a))
d = {1:100,2:200,3:300,4:400,5:500}
print(d)
print(d[2])
print(d.get(4))
print(d.keys())
print(d.values())
del d[3]
print(d)
d.clear()
len(d)

#tuple
t=(100,200,300,400)
print(t)
print(t[0])
print(t[3])
print(t.index(200))
t2=(10,20,10,30,10,40,20)
print(t2.count(20))
print(t2.count(10))
print(t2.count(30))

#penambahan
# contoh1
himpunan_nama_siswa = {'Nawang', 'Bella', 'Agnes', 'Vera'}
print(himpunan_nama_siswa)

# contoh2
himpunan_nama_buah = set(['apple', 'cherry', 'bluberry'])
print(himpunan_nama_buah)

#contoh3
himpunan_huruf_abjad = {'a', 'b', 'c'}
print(himpunan_huruf_abjad)

# menambah satu-satu
himpunan_huruf_abjad.add('d')
himpunan_huruf_abjad.add('e')
himpunan_huruf_abjad.add('f')
himpunan_huruf_abjad.add('g')
himpunan_huruf_abjad.add('h')
himpunan_huruf_abjad.add('i')
himpunan_huruf_abjad.add('j')

# menambah lebih dari satu anggota sekaligus
himpunan_huruf_abjad.update({ 'k', 'l' })

# bisa juga pakai list
himpunan_huruf_abjad.update(['m', 'n'])

print(himpunan_huruf_abjad)

#contoh4
# set integer 
my_set = {5,6,9} 
print(my_set) 

# set dengan menggunakan fungsi set() 
my_set = set([7,8,10]) 
print(my_set) 

# set data campuran 
my_set1 = {1, 2.0, "Python", (3,4,5)} 
print(my_set1) 

my_set2 = {'Human', 'Animals', 12, True, ('Y', 'N')}
print(my_set2)
