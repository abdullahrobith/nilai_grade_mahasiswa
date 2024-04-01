print(10*'📌','Menghitung Grade Mahasiswa',10*'📌')
nama = str(input('Nama Mahasiswa : '))
nilai_akhir = float(input("Masukkan nilai akhir mahasiswa: "))
if nilai_akhir >= 85:
    grade = "A"
elif nilai_akhir >= 70:
    grade = "B"
elif nilai_akhir >= 55:
    grade = "C"
elif nilai_akhir >= 40:
    grade = "D"
else:
    grade = "E"
print(nama, 'Mendapatkan nilai grade : ', grade)
print(10*'🎓','Sekian😉',10*'🎓')