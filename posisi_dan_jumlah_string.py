teks = "Apel malang adalah apel termanis dibanding apel-apel lainnya"
# Fitur .find() Mengembalikan posisi dr sebuah teks(sub-string) lainnya dalam sebuah string
print(">>> Fitur .find()")
print(teks.find("Apel")) #Output Apel karna kalimat diawali dengan kata Apel
print(teks.find("malang")) # Output Malang karena kata malang muncul dimulai dari index ke 5 jika teks dijadikan array
# Fitur .count() Menghitung jumlah kemunculan sebuah teks(string) lainnya dalam suatu string (string yg dicari bersifat case sensitive)
print(">>> Fitur .count()")
kemunculan_kata_apel = teks.count("apel")
print(kemunculan_kata_apel) # Output 3 karena dalam teks adanya Apel, sedangkan count apel, huruf kapital tidak dihitung karna tidak sama