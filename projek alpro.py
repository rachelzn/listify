import json
import os

def simpan_akun(username, password):
    with open("akun.txt", "a") as f:
        f.write(f"{username},{password}\n")

def login(username, password):
    if not os.path.exists("akun.txt"):
        return False
    with open("akun.txt", "r") as f:
        for line in f:
            user, pw = line.strip().split(",")
            if username == user and password == pw:
                return True
    return False

def load_tugas():
    if os.path.exists("tugas.txt"):
        with open("tugas.txt", "r") as f:
            return json.load(f)
    return []

def simpan_tugas():
    with open("tugas.txt", "w") as f:
        json.dump(tugas_list, f, indent=2)

while True:
    print("=====LISTIFY=====")
    print("1. Login")
    print("2. Register")
    pilihan = input("Pilih (1/2): ")

    if pilihan == "1":
        nama = input("Masukkan nama: ")
        password = input("Masukkan password (6 digit angka saja): ")

        if login(nama, password):
            print(f"\nHi {nama}!")
            print("Jangan lupa kerjakan tugasmu bestie :)")
            break
        else:
            print("Login gagal! Username atau password salah.\n")

    elif pilihan == "2":
        nama = input("Buat nama pengguna: ")
        while True:
            password = input("Buat password (6 digit angka): ")
            if password.isdigit() and len(password) == 6:
                break
            print("Password harus berupa 6 digit angka.")
        simpan_akun(nama, password)
        print("Registrasi berhasil! Silakan login.\n")
    else:
        print("Pilihan tidak valid.\n")

input("Enter untuk melanjutkan...")

tugas_list = load_tugas()

def tambah_tugas(nama_tugas, deskripsi_tugas, deadline, status_tugas):
    tugas = {
        "nama_tugas": nama_tugas,
        "deskripsi_tugas": deskripsi_tugas,
        "deadline": deadline,
        "status_tugas": status_tugas
    }
    tugas_list.append(tugas)
    simpan_tugas()

def lihat_daftar_tugas():
    if not tugas_list:
        print("Belum ada tugas.")
    else:
        for i, tugas in enumerate(tugas_list):
            print(f"{i+1}. {tugas['nama_tugas']} - {tugas['deadline']} - {tugas['status_tugas']}")

def edit_tugas(index, nama_tugas, deskripsi_tugas, deadline, status_tugas):
    if 0 <= index < len(tugas_list):
        tugas_list[index] = {
            "nama_tugas": nama_tugas,
            "deskripsi_tugas": deskripsi_tugas,
            "deadline": deadline,
            "status_tugas": status_tugas
        }
        simpan_tugas()
    else:
        print("Indeks tugas tidak valid!")

def hapus_tugas(index):
    if 0 <= index < len(tugas_list):
        del tugas_list[index]
        simpan_tugas()
    else:
        print("Indeks tugas tidak valid!")

def menandai_tugas_selesai(index):
    if 0 <= index < len(tugas_list):
        tugas_list[index]["status_tugas"] = "selesai"
        simpan_tugas()
    else:
        print("Indeks tugas tidak valid!")

while True:
    print("\n=== Menu Tugas ===")
    print("1. Tambah Tugas")
    print("2. Lihat Daftar Tugas")
    print("3. Edit Tugas")
    print("4. Tandai Tugas Selesai")
    print("5. Hapus Tugas")
    print("6. Logout")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("\n===Tambah Tugas===")
        nama_tugas = input("Nama tugas: ")
        deskripsi_tugas = input("Deskripsi tugas: ")
        deadline = input("Deadline: ")
        status_tugas = "belum selesai"
        tambah_tugas(nama_tugas, deskripsi_tugas, deadline, status_tugas)

    elif pilihan == "2":
        print("\n===Lihat Daftar Tugas===")
        lihat_daftar_tugas()

    elif pilihan == "3":
        print("\n===Edit Tugas===")
        lihat_daftar_tugas()
        try:
            index = int(input("Pilih nomor tugas untuk diedit: ")) - 1
            nama_tugas = input("Nama tugas baru: ")
            deskripsi_tugas = input("Deskripsi tugas baru: ")
            deadline = input("Deadline baru: ")
            status_tugas = input("Status tugas (selesai/belum selesai): ")
            edit_tugas(index, nama_tugas, deskripsi_tugas, deadline, status_tugas)
        except ValueError:
            print("Masukkan angka yang valid.")

    elif pilihan == "4":
        print("\n===Tandai Tugas Selesai===")
        lihat_daftar_tugas()
        try:
            index = int(input("Pilih nomor tugas yang selesai: ")) - 1
            menandai_tugas_selesai(index)
        except ValueError:
            print("Masukkan angka yang valid.")

    elif pilihan == "5":
        print("\n===Hapus Tugas===")
        lihat_daftar_tugas()
        try:
            index = int(input("Pilih nomor tugas untuk dihapus: ")) - 1
            hapus_tugas(index)
        except ValueError:
            print("Masukkan angka yang valid.")

    elif pilihan == "6":
        print("\nLogout berhasil. Sampai jumpa lagi bestie ✨")
        break

    else:
        print("Pilihan tidak valid!")
