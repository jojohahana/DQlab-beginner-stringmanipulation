# Fitur .append() Menambahkan data sebagai elemen terakhir di list
# Menambahkan list pada element terakhir
print(">>> Fitur .append()")
list_makanan = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_makanan.append('Ketoprak')
print(list_makanan)


# Fitur .clear() Mengapus seluruh elemen dalam sebuah list
print(">>> Fitur .clear()")
list_makanan = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_makanan.clear()
print(list_makanan)


# Fitur .copy() Mengembalikan copy dari setiap elemen dalam list
print(">>> Fitur .copy()")
list_makanan1 = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_makanan2 = list_makanan1.copy() #copy list_makanan1 dijadikan variable list_makanan2
list_makanan3 = list_makanan1 #list makanan3 isinya sama dengan list_makanan1
list_makanan2.append('Opor') #ditambahkan opor ke list_makanan2
list_makanan3.append('Ketoprak') #ditambahkan ketoprak ke list_makanan3
print(list_makanan1)
print(list_makanan2)
print(list_makanan3)


# Fitur .count() Mengembalikan jumlah kemunculan suatu element pada list
print(">>> Fitur .count()")
list_score = ['Budi', 'Sud', 'Budi', 'Budi', 'Budi', 'Sud', 'Sud']
score_budi = list_score.count('Budi')
score_sud = list_score.count('Sud')
print(score_budi) # akan menampilkan output 4
print(score_sud) # akan menampilkan output 3


# Fitur .extend() Menggabungkan dua list, seperti penggunaan operator + pada list
print(">>> Fitur .extend()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_minuman = ['Es Teh', 'Es Jeruk', 'Es Campur']
list_menu.extend(list_minuman)
print(list_menu)