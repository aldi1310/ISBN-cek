# Meminta input 12 digit pertama nomor ISBN-13
ISBN = input ('Masukkan 12 digit nomor ISBN : ')

# Mengambil setiap digit dan mengalikannya dengan bobot sesuai aturan ISBN-13
n1 = int(ISBN[0]) * 1     # digit ke-1 × 1
n2 = int(ISBN[1]) * 3     # digit ke-2 × 3
n3 = int(ISBN[2]) * 1     # digit ke-3 × 1
n4 = int(ISBN[3]) * 3     # digit ke-4 × 3
n5 = int(ISBN[4]) * 1     # digit ke-5 × 1
n6 = int(ISBN[5]) * 3     # digit ke-6 × 3
n7 = int(ISBN[6]) * 1     # digit ke-7 × 1
n8 = int(ISBN[7]) * 3     # digit ke-8 × 3
n9 = int(ISBN[8]) * 1     # digit ke-9 × 1
n10 = int(ISBN[9]) * 3    # digit ke-10 × 3
n11 = int(ISBN[10]) * 1   # digit ke-11 × 1
n12 = int(ISBN[11]) * 3   # digit ke-12 × 3

# Menjumlahkan hasil semua perkalian
sum = (n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12)

# Menghitung check digit ISBN-13:
# Rumus: (10 - (jumlah % 10)) % 10
n13 = 10 - (sum % 10)

# Menampilkan jumlah (opsional)
print(sum)

# Menampilkan digit cek ISBN-13
print('Cek digit : '+str(n13))

