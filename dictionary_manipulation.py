# Fitur .clear() Menghapus semua elemen dictionary
print(">>> Fitur .clear()")
info_karyawan = {'nama' : 'Aksara', # key:value
                 'nik' : '1211011',
                 'pekerjaan' : 'Data Analyst'}
info_karyawan.clear()
print(info_karyawan)

# Fitur .copy() Mengembalikan copy dari setiap data set
print(">>> Fitur .copy()")
info_karyawan1 = {'nama' : 'Aksara',
                  'nik' : '1211011',
                  'pekerjaan' : 'Data Analyst'}
info_karyawan2 = info_karyawan1.copy()
info_karyawan2['nama'] = 'Senja' #Update key & value dari Aksara diganti menjadi  Senja
info_karyawan2['nik'] = '1211056' #update mengikuti key & value diatas
print(info_karyawan1)
print(info_karyawan2)

# Fitur .keys() Mengembalikan list dari seluruh key dr setiap elemen
print(">>> Fitur .keys()")
info_karyawan = {'nama' : 'Aksara',
                 'nik' : '1211011',
                 'pekerjaan' : 'Data Analyst'}
kunci_akses = list(info_karyawan.keys())
print(kunci_akses)

# Fitur .values() Mengembalikan list dr seluruh nilai value dr setiap elemen 
print(">>> Fitur .values()")
value_dict = list(info_karyawan.values())
print(value_dict) # Output hanya menampilkan nilai value

# Fitur .update() Menambahkan key & nilai baru value 
print(">>> Fitur .update()")
info_karyawan.update({'skillset':['Python', 'R']})
print(info_karyawan)