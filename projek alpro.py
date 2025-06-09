# Login
nama = input("Masukkan nama: ")
password = input("Masukkan password (6 digit angka saja): ")

while not password.isdigit() or len(password) != 6:
    print("Password harus berupa 6 digit angka saja!")
    password = input("Masukkan password (6 digit angka saja): ")

if nama and password:
    print(f"Hi {nama}!")
    print("Jangan Lupa kerjakan tugas mu bestie :)")
else:
    print("Nama dan password tidak boleh kosong!")
    exit()

input("Enter untuk melanjutkan...")

# List tugas
tugas_list = []

# Fungsi tambah tugas
def tambah_tugas(nama_tugas, deskripsi_tugas, deadline, status_tugas):
    tugas = {
        "nama_tugas": nama_tugas,
        "deskripsi_tugas": deskripsi_tugas,
        "deadline": deadline,
        "status_tugas": status_tugas
    }
    tugas_list.append(tugas)

# Fungsi lihat daftar tugas
def lihat_daftar_tugas():
    for i, tugas in enumerate(tugas_list):
        print(f"{i+1}. {tugas['nama_tugas']} - {tugas['deadline']} - {tugas['status_tugas']}")

# Fungsi edit tugas
def edit_tugas(index, nama_tugas, deskripsi_tugas, deadline, status_tugas):
    tugas_list[index]["nama_tugas"] = nama_tugas
    tugas_list[index]["deskripsi_tugas"] = deskripsi_tugas
    tugas_list[index]["deadline"] = deadline
    tugas_list[index]["status_tugas"] = status_tugas

# Fungsi hapus tugas
def hapus_tugas(index):
    del tugas_list[index]

# Fungsi menandai tugas selesai
def menandai_tugas_selesai(index):
    tugas_list[index]["status_tugas"] = "selesai"

# Fungsi pilih tema
def pilih_tema(index):
    global current_bg, current_fg

# Main program
while True:
    print("1. Tambah Tugas")
    print("2. Lihat Daftar Tugas")
    print("3. Edit Tugas")
    print("4. Hapus Tugas")
    print("5. Menandai Tugas Selesai")
    print("6. pilih tema")
    print ("7. Logout")
    
    pilihan = input("Pilih menu: ")
    
    if pilihan == "1":
        nama_tugas = input("Nama tugas: ")
        deskripsi_tugas = input("Deskripsi tugas: ")
        deadline = input("Deadline: ")
        status_tugas = "belum selesai"
        tambah_tugas(nama_tugas, deskripsi_tugas, deadline, status_tugas)
    elif pilihan == "2":
        lihat_daftar_tugas()
    elif pilihan == "3":
        index = int(input("Pilih tugas yang ingin diedit: ")) - 1
        nama_tugas = input("Nama tugas: ")
        deskripsi_tugas = input("Deskripsi tugas: ")
        deadline = input("Deadline: ")
        status_tugas = input("Status tugas: ")
        edit_tugas(index, nama_tugas, deskripsi_tugas, deadline, status_tugas)
    elif pilihan == "4":
        index = int(input("Pilih tugas yang ingin dihapus: ")) - 1
        hapus_tugas(index)
    elif pilihan == "5":
        index = int(input("Pilih tugas yang ingin ditandai selesai: ")) - 1
        menandai_tugas_selesai(index)
    elif pilihan == "6":
        pilihan_tema = input("Masukkan pilihan tema (1/2): ")
    if pilihan_tema == "1":
        "kuning"
        print("Tema kuning dipilih.")
    elif pilihan_tema == "2":
       "pink"
       print("Tema pink dipilih.")
    elif pilihan == "7":
        print("Terima kasih telah list tugasmu ingat deadline mu bestie :)")
        break
    else:
        print("Pilihan tidak valid")
        