# 'List' data type example
x = ['Katib Pasha', 20, 'Desktop Programming', 3.99]

# Index test
'''print(x[2])'''  # --> return : Desktop Programming

# 'Tuple' data type example
y = ('Desktop Programming', 20, 'Katib Pasha', 3.99)
'''print(y[2]) '''  # return: Katib Pasha

# immutable test
'''y[2] = 'Katib Nurkandam'  # intented to change index-2 with new value
print(y[2])  # return: error'''

# 'Set' data type example
z = {2, 9, 1, 4, 5, 3, 5}
'''print(type(z))'''  # return: <class 'set>

# unique value test
'''print(z)'''  # double value of 5 will show once only --> {1,2,3,4,5,9}

# 'Dictionary' data type example
a = {'name': 'Katib Pasha', 'division': 'Desktop Programming', 'age': 20, 'IP': 3.99}

# get age object
'''print(a.get('age'))'''  # --> return: 20

# ------------------------------------------

# Input section
'''panjang = input('Masukkan nilai panjang: ')
lebar = input('Masukkan nilai lebar: ')
'''
# calculation and data type conversion
'''luas = int(panjang) * int(lebar)
print("Luas =", luas)'''

# ------------------------------------------

# Function
# example of static function


def halo_dunia():
    print('Halo python! Halo dunia!')


halo_dunia()  # --> return: will operate the 'halo_dunia()' function

# example of dynamic function


def perkenalan(nama, asal):
    print(f"Perkenalkan saya {nama} dari {asal}")


# --> call 'perkenalan' function + add parameter value
perkenalan('Katib Pasha', 'Malaysia')
