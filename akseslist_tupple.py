#Collection Manipulation
#Akses list & tuple pada python


bulan_pembelian = ('Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember')
pertengahan_tahun = bulan_pembelian[4:8] #akses middle years
print(pertengahan_tahun)
awal_tahun = bulan_pembelian[:5] #akses index awal sampai index 5
print(awal_tahun)
akhir_tahun = bulan_pembelian[8:] #akses start index 8 sampai akhir
print(akhir_tahun)
print(bulan_pembelian[-4:-1]) #motong list/tuple menggunakan index negatif
print(bulan_pembelian[:-3]) #potong index dari list blkang start index 0 sampai -2
    #hasil diatas adalah bulan_pembelian dikurangi index :-3