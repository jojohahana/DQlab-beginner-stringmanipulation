#Untuk menentukan berapa jumlah data yang tersimpat pada elemen tuple
#Gunakan fungsi built-in len()
# Tuple
print(">>> Tuple")
tuple_menu = ('Gado-gado','Ayam Goreng','Rendang','Ketoprak')
jumlah_menu = len(tuple_menu) # Hitung jumlah data menu
print(jumlah_menu)
# List
print(">>> List")
list_menu = ['Gado-gado','Ayam Goreng','Rendang','Ketoprak']
jumlah_menu = len(list_menu) # Hitung jumlah data menu
print(jumlah_menu)
# Konversi tipe data
#Konversi data collection
print(">>> Konversi tipe data")
list_buah = ['Apel', 'Apel', 'Jeruk', 'Markisa', 'Jeruk', 'Markisa', 'Apel']
set_buah = set(list_buah) #konversi dari list ke set, kalau set ga boleh ada duplicat value dlm satu set
print(set_buah)
list_buah = list(set_buah) #konversi dari set menjadi sebuah list
list_buah.sort()
print(list_buah)