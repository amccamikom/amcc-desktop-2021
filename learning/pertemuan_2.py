# Boolean data type (tanpa tanda "..")
"""x = False

print(x)"""


# ---------------------------------------------
# Operator Comparison (penerapannya ada pada if-else)

# Operator Assignment
"""a = 5
a -= 2

print(a)"""

# Operator Logical
"""hasil = not (5 < 3 or 10 < 4)
print(hasil)"""

# Operator Identity
"""a = 8
b = 5

# output True
print('a is not b:', a is not b)
"""


# ---------------------------------------------
# Percabangan (conditional)
"""Diterima = 'Ya'

if Diterima == 'No':
    print('Sudah Jangan Sedih Yah')"""

"""jumlah = int(input('Berapa Jumlah Doi Kamu?: '))
if jumlah >= 4:
    print('Kamu Fucekboy ah')
else:
    print('Gini Dong Setia')"""

"""nilai = int(input('Berapa Nilai Kamu?: '))
if nilai >= 81 and nilai <= 100:
    Grade = 'A'
elif nilai >= 61 and nilai <= 80:
    Grade = 'B'
elif nilai >= 51 and nilai <= 60:
    Grade = 'C'
elif nilai >= 41 and nilai <= 50:
    Grade = 'D'
else:
    Grade = 'E'
print(Grade)"""


# ---------------------------------------------
# Perulangan (looping)
"""ulang = int(input('Berapa kali diulang?: '))

for x in range(ulang):
    print('perulangan ke-' + str(x+1))"""

"""jawab = input("jawaban kamu apa?: ")
hitung = 0

while(jawab == 'ya'):
    hitung += 1
    jawab = input('Ulang lagi tidak?: ')

print('Total perulangan: '+str(hitung))"""

nama = "Mikail"
kampus = 'Universitas AMIKOM Yogykarta'

print(nama + ' - ' + kampus)
