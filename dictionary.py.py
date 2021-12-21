arr = [9,4,3,7,8]
cari = int(input('nilai yang di cari :'))
posisi = 0
iterasi = 0
akhir = len(arr)-1
found = False
while posisi<= akhir and not found:
    iterasi +=1
    if arr[posisi] == cari:
        found = True
    else: posisi = posisi + 1
if found:
    print("angka yang anda cari terletak pada indeks :",posisi)
    print("iterasi sebanyak =",iterasi,"kali")
else:
    print("nomor yang di cari tidak ditemukan")
    print("iterasi sebanyak",iterasi,"kali")
   

        
