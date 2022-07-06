#belajar string
kata = "umar"
print(kata)

kata = kata.lower()
print("Kata jadi lowercase : " + kata)

#cek lower
cek_lower = kata.islower()
print("Kata jadi lowercase : " + str(cek_lower))

kata = kata.upper()
print("Kata jadi uppercase : " + kata)

#cek upper
cek_upper = kata.isupper()
print("Kata jadi uppercase : " + str(cek_upper))

#coba gabung
buah = ['mangga', 'strawberry', 'lemon']
gabungan = ' '.join(buah)
print(gabungan)

#coba pisah
buah = "mangga anggur leci"
pisah = buah.split(" ")
print(pisah)

#text alignment
text = "coba".rjust(20)
print(text)
text = "coba".ljust(20)
print(text)
text = "coba".center(20,"0")
print(text)