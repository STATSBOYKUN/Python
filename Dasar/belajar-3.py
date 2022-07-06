import datetime as dt

print("Input data")

hari = int(input("Tanggal = "))
bulan = int(input("Bulan = "))
tahun = int(input("Tahun = "))

print(dt.date(tahun,bulan,hari))
print(dt.date.today()) 