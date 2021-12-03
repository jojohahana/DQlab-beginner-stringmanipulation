# Fitur .count() Mengembalikan jumlah kemunculan suatu element pada tuple
print(">>> Fitur .count()")
tuple_score = ('Budi', 'Sud', 'Budi', 'Budi', 'Budi', 'Sud', 'Sud')
score_budi = tuple_score.count('Budi')
score_sud = tuple_score.count('Sud')
print(score_budi) # akan menampilkan output 4
print(score_sud) # akan menampilkan output 3


# Fitur .index() Mengembalikan indeks dari elemen pertama yang ditemukan dr awal sebuah tuple
print(">>> Fitur .index()")
tuple_score = ('Budi','Sud','Budi','Budi','Budi','Sud','Sud')
score_pertama_sud = tuple_score.index('Sud')+1 #index Sud + 1
print(score_pertama_sud) # akan menampilkan output 2