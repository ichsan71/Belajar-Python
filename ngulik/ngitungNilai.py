# Input User
kehadiran = int(input("asup keun kehadiran maneh! [0..16]: "))
Nilai_TGS = int(input("asup keun Nilai Tugas maneh! : "))
Nilai_UTS = int(input("asup keun Nilai UTS maneh! : "))
Nilai_UAS = int(input("asup keun Nilai UAS maneh! : "))
print("------------------------------------------------")

# Formula
Nilai_kehadiran = kehadiran / 16 * 100
Nilai_Akhir = (0.1 * Nilai_kehadiran) + (0.2 * Nilai_TGS) + (0.3 * Nilai_UTS) + (0.4 * Nilai_UAS)

#Pengkondisian
if Nilai_Akhir >= 80 and Nilai_Akhir <= 100:
    index = "A"
    Keterangan = "Sangat baik"
elif Nilai_Akhir >= 68 and Nilai_Akhir < 80:
    index = "B"
    Keterangan = "Baik"
elif Nilai_Akhir >= 56 and Nilai_Akhir < 68:
    index = "C"
    Keterangan = "Cukup" 
elif Nilai_Akhir >= 45 and Nilai_Akhir < 56:
    index = "D"
    Keterangan = "Kurang"
elif Nilai_Akhir >= 0 and Nilai_Akhir < 45:
    index = "E"
    Keterangan = "Sangat Kurang"
else:
    print("Nilai tidak sah!")

# Output
print("Nilai Kehadiran maneh sakieu : " + str(Nilai_kehadiran))
print("Nilai Akhir maneh sakieu : " + str(Nilai_Akhir))
print("Index        : " + index)
print("Keterangan   : " + Keterangan)