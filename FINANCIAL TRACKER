import csv
from datetime import datetime

def load_transactions(filename="transactions.csv"):
    data = []
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data

    except FileNotFoundError:
        print("[INFO] File CSV tidak ditemukan, membuat file baru...")
        return []

    except Exception:
        print("[ERROR] CSV Format Error – File corrupt.")
        return []


def save_transactions(data, filename="transactions.csv"):
    header = ["tanggal", "jenis", "kategori", "jumlah", "catatan"]
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            writer.writerows(data)
        print("[SUCCESS] Data berhasil disimpan.")
    except Exception:
        print("[ERROR] Gagal menyimpan data ke CSV.")


def validate_amount(value):
    try:
        amount = float(value)
        if amount <= 0:
            raise ValueError
        return amount
    except ValueError:
        print("Jumlah uang tidak valid! Harus angka positif.")
        return None


def validate_date(value):
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return value
    except ValueError:
        print("Format tanggal salah! Gunakan format YYYY-MM-DD.")
        return None


def tambah_transaksi(data):
    print("\n=== Tambah Transaksi ===")

    tanggal = None
    while tanggal is None:
        tanggal_input = input("Tanggal (YYYY-MM-DD): ")
        tanggal = validate_date(tanggal_input)

    jenis = input("Jenis (pemasukan/pengeluaran): ").lower()

    kategori = input("Kategori: ")

    jumlah = None
    while jumlah is None:
        jumlah_input = input("Jumlah: ")
        jumlah = validate_amount(jumlah_input)

    catatan = input("Catatan (opsional): ")

    transaksi = {
        "tanggal": tanggal,
        "jenis": jenis,
        "kategori": kategori,
        "jumlah": jumlah,
        "catatan": catatan
    }

    data.append(transaksi)
    print("[SUCCESS] Transaksi berhasil ditambahkan!")


def lihat_transaksi(data):
    print("\n=== Lihat Transaksi ===")
    print("1. Semua transaksi")
    print("2. Hanya pemasukan")
    print("3. Hanya pengeluaran")

    pilihan = input("Pilih: ")

    print("\n--- Daftar Transaksi ---")
    for d in data:
        if pilihan == "2" and d["jenis"] != "pemasukan":
            continue
        if pilihan == "3" and d["jenis"] != "pengeluaran":
            continue

        print(f"{d['tanggal']} | {d['jenis']} | {d['kategori']} | Rp{d['jumlah']} | {d['catatan']}")


def laporan_bulanan(data):
    print("\n=== Laporan Bulanan ===")
    bulan = input("Masukkan bulan (01-12): ")
    tahun = input("Masukkan tahun (YYYY): ")

    pemasukan = 0
    pengeluaran = 0
    kategori_spending = {}

    for d in data:
        if d["tanggal"].startswith(f"{tahun}-{bulan}"):
            jumlah = float(d["jumlah"])

            if d["jenis"] == "pemasukan":
                pemasukan += jumlah
            else:
                pengeluaran += jumlah
                kategori_spending[d["kategori"]] = kategori_spending.get(d["kategori"], 0) + jumlah

    saldo = pemasukan - pengeluaran
    saving_rate = (saldo / pemasukan * 100) if pemasukan > 0 else 0

    print("\n--- Laporan Bulanan ---")
    print(f"Total pemasukan : Rp{pemasukan}")
    print(f"Total pengeluaran : Rp{pengeluaran}")
    print(f"Saldo akhir : Rp{saldo}")
    print(f"Tingkat saving : {saving_rate:.2f}%")

    if kategori_spending:
        top_category = max(kategori_spending, key=kategori_spending.get)
        print(f"Kategori pengeluaran terbesar: {top_category} (Rp{kategori_spending[top_category]})")


def export_data(data):
    filename = "export_finance.csv"
    try:
        save_transactions(data, filename)
    except Exception:
        print("[ERROR] Gagal export data.")


def dashboard(data):
    pemasukan = sum(float(d["jumlah"]) for d in data if d["jenis"] == "pemasukan")
    pengeluaran = sum(float(d["jumlah"]) for d in data if d["jenis"] == "pengeluaran")
    saldo = pemasukan - pengeluaran

    print("\n=== Dashboard ===")
    print(f"Saldo saat ini : Rp{saldo}")
    print("\n5 Transaksi Terbaru:")
    for d in data[-5:]:
        print(f"- {d['tanggal']} | {d['jenis']} | Rp{d['jumlah']}")


def main_menu():
    data = load_transactions()

    while True:
        print("\n=== Simple Personal Finance Tracker ===")
        print("1. Tambah transaksi")
        print("2. Lihat transaksi")
        print("3. Laporan bulanan")
        print("4. Dashboard")
        print("5. Export data CSV")
        print("6. Simpan & Keluar")

        pilihan = input("Pilih menu: ")

        try:
            if pilihan == "1":
                tambah_transaksi(data)
            elif pilihan == "2":
                lihat_transaksi(data)
            elif pilihan == "3":
                laporan_bulanan(data)
            elif pilihan == "4":
                dashboard(data)
            elif pilihan == "5":
                export_data(data)
            elif pilihan == "6":
                save_transactions(data)
                print("Sampai jumpa!")
                break
            else:
                print("Pilihan tidak valid.")

        except KeyboardInterrupt:
            print("\n[ERROR] Program dihentikan paksa.")
            break


if __name__ == "__main__":
    main_menu()
