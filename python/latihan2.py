# Latihan 2 Python : Input User & Pengkondisian (If-Else)

# Mengambil input dari user
nama_pelamar = "Arya"
skor_excel = 85 # Contoh nilai keahlian Excel/Spreadsheet (skala 1-100)

print("--- EVALUASI KUALIFIKASI WFH ---")
print("Nama Pelamar:", nama_pelamar)
print("Skor Keahlian Spreadsheet:", skor_excel)

#Logika Pengkondisian (If-Else)
if skor_excel >= 80:
  status = "Siap melamar posisi WFH Data Associate / Admin Specialist!"
elif skor_excel >= 60:
  status = "Perlu sedikit latihan tambahan fungsi VLOOKUP & Pivot Table."
else:
  status = "Fpkus pelajari dasar-dasar spreadsheet terlebih dahulu.

print("Hasil Evaluasi:", status)
