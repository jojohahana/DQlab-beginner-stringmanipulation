# Fitur .split() Memecah sebuah string berdasarkan string lainnya kedalam sebuah list
print(">>> Fitur .split()")
bilangan = "ani dan budi dan wati dan johan"
karakter = bilangan.split("dan")
print(karakter)
kata = bilangan.split(" ")
print(kata)
# Fitur .join() Menggabungkan list yg berisikan string berdasarkan sebuah string yang telah didefinisikan 
print(">>> Fitur .join()")
pemisah = " dan "
karakter = ["Ricky", "Peter", "Jordan"]
kalimat = pemisah.join(karakter)
print(kalimat)
# Fitur .replace() Menggabungkan sebuah list string pada sebiah string yg telah didefinisikan
print(">>> Fitur .replace()")
kalimat = "apel malang apel yang paling segar, apel sehat, apel nikmat"
kalimat = kalimat.replace("apel", "jeruk")
print(kalimat)