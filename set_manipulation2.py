# Fitur .union() Mengembalikan hasil penggabungan(union) dari 2 buah data set 
print(">>> Fitur .union()")
parcel1 = {'Anggur','Apel','Jeruk'}
parcel2 = {'Apel','Kiwi','Melon'}
parcel3 = parcel1.union(parcel2)
print(parcel1)
print(parcel3)


# Fitur .isdisjoint() Mengembalikan nilai kebenaran apakah suatu set disjoint(tidak mengandung elemen sama) dengan set lainnya
print(">>> Fitur .isdisjoint()")
parcel1 = {'Anggur','Apel','Jeruk'}
parcel2 = {'Kiwi','Melon','Pisang'}
parcel3 = {'Apel','Srikaya','Semangka'}
parcel1_parcel2_disjoint = parcel1.isdisjoint(parcel2)
print(parcel1_parcel2_disjoint)
parcel1_parcel3_disjoint = parcel1.isdisjoint(parcel3)
print(parcel1_parcel3_disjoint)


# Fitur .issubset() Mengembalikan nilai kebeneran apakah sebuah set mengandung subset lainnya
print(">>> Fitur .issubset()") 
parcel_A = {'Anggur', 'Apel'}
parcel_B = {'Durian','Semangka','Apel'}
parcel_C = {'Anggur', 'Kiwi', 'Apel', 'Jeruk', 'Melon'}
parcel_A_dalam_C = parcel_A.issubset(parcel_C)# Output True karna di A dan C ada Apel
parcel_B_dalam_C = parcel_B.issubset(parcel_C) # Output False karna B tidak ada isi yg sama dengan C
print(parcel_A_dalam_C)
print(parcel_B_dalam_C)


# Fitur .issuperset() Mengembalikan nilai kebenaran apakah sebuah set merupakan superset dari set lainnya
print(">>> Fitur .issuperset()")
parcel_C_mengandung_A = parcel_C.issuperset(parcel_A)
parcel_C_mengandung_B = parcel_C.issuperset(parcel_B)
print(parcel_C_mengandung_A) # Output True karna isi set C mengandung seluruh elemen A
print(parcel_C_mengandung_B) # Output False karna 


# Fitur .intersection() Mengembalikan sebuah set yg merupakan intersection dari 2 set lainnya
print(">>> Fitur .intersection()")
parcel_A = {'Anggur', 'Kiwi', 'Apel', 'Jeruk', 'Melon'}
parcel_B = {'Apel', 'Jeruk', 'Semangka', 'Durian', 'Tomat'}
parcel_C = parcel_A.intersection(parcel_B)
print(parcel_C) #Output Jeruk & Apel karna ada di A & B


# Fitur .difference() Difference adalah setiap elemen pada set A tidak terdapat pada set B
print(">>> Fitur .difference()")
parcel_C = parcel_A.difference(parcel_B)
print(parcel_C) #Output Anggur, Kiwi, Melon karna Apel & Jeruk ada di B


# Fitur .symmetric_difference() Setiap elemen A tidak terdapat di B digabungkan(union) dr elemen B yg tidak ada di A
print(">>> Fitur .symmetric_difference()")
parcel_A = {'Anggur', 'Apel', 'Jeruk', 'Melon'}
parcel_B = {'Apel','Jeruk','Semangka','Leci'}
parcel_C = parcel_A.symmetric_difference(parcel_B) 
print(parcel_C) #Output Anggur, Melon, Semangka, Leci -> kecuali Apel & Jeruk yg ada di A & B