import csv
import os

FILENAME = "students.csv"
EXPORT_FOLDER = "exports"

FIELDS = [
    "nim",
    "nama",
    "kelas",
    "tugas",
    "uts",
    "uas",
    "rata_rata",
    "grade"
]


def load_students(filename=FILENAME):
    students = []

    if not os.path.exists(filename):
        return students

    try:
        with open(
            filename,
            mode="r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:
                students.append(row)

    except (OSError, csv.Error):
        print("[ERROR] Gagal membaca file data.")

    return students


def save_students(students, filename=FILENAME):
    try:
        with open(
            filename,
            mode="w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=FIELDS
            )

            writer.writeheader()
            writer.writerows(students)

        print("[SUCCESS] Data berhasil disimpan.")

    except OSError:
        print("[ERROR] Gagal menyimpan data.")


def input_score(label):
    while True:
        try:
            score = float(input(f"{label}: "))

            if 0 <= score <= 100:
                return score

            print("Nilai harus berada di antara 0 dan 100.")

        except ValueError:
            print("Input harus berupa angka.")


def calculate_average(tugas, uts, uas):
    return (
        tugas * 0.30
        + uts * 0.30
        + uas * 0.40
    )


def calculate_grade(average):
    if average >= 85:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 65:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "E"


def find_student(students, nim):
    for student in students:
        if student["nim"] == nim:
            return student

    return None


def add_student(students):
    print("\n=== TAMBAH DATA MAHASISWA ===")

    nim = input("NIM   : ").strip()

    if not nim:
        print("[ERROR] NIM tidak boleh kosong.")
        return

    if find_student(students, nim):
        print("[ERROR] NIM sudah terdaftar.")
        return

    nama = input("Nama  : ").strip()

    if not nama:
        print("[ERROR] Nama tidak boleh kosong.")
        return

    kelas = input("Kelas : ").strip()

    if not kelas:
        print("[ERROR] Kelas tidak boleh kosong.")
        return

    tugas = input_score("Nilai Tugas")
    uts = input_score("Nilai UTS")
    uas = input_score("Nilai UAS")

    average = calculate_average(
        tugas,
        uts,
        uas
    )

    grade = calculate_grade(average)

    student = {
        "nim": nim,
        "nama": nama,
        "kelas": kelas,
        "tugas": f"{tugas:.2f}",
        "uts": f"{uts:.2f}",
        "uas": f"{uas:.2f}",
        "rata_rata": f"{average:.2f}",
        "grade": grade
    }

    students.append(student)

    save_students(students)

    print("[SUCCESS] Data mahasiswa berhasil ditambahkan.")


def display_students(students):
    if not students:
        print("\n[INFO] Belum ada data mahasiswa.")
        return

    print("\n=== DAFTAR NILAI MAHASISWA ===")

    print("-" * 90)

    print(
        f"{'NIM':<12}"
        f"{'Nama':<20}"
        f"{'Kelas':<10}"
        f"{'Tugas':>8}"
        f"{'UTS':>8}"
        f"{'UAS':>8}"
        f"{'Rata-rata':>11}"
        f"{'Grade':>7}"
    )

    print("-" * 90)

    for student in students:
        print(
            f"{student['nim']:<12}"
            f"{student['nama'][:19]:<20}"
            f"{student['kelas'][:9]:<10}"
            f"{student['tugas']:>8}"
            f"{student['uts']:>8}"
            f"{student['uas']:>8}"
            f"{student['rata_rata']:>11}"
            f"{student['grade']:>7}"
        )

    print("-" * 90)


def search_student(students):
    print("\n=== CARI MAHASISWA ===")

    nim = input("Masukkan NIM: ").strip()

    student = find_student(
        students,
        nim
    )

    if not student:
        print("[INFO] Data mahasiswa tidak ditemukan.")
        return

    print("\n=== DATA MAHASISWA ===")
    print(f"NIM         : {student['nim']}")
    print(f"Nama        : {student['nama']}")
    print(f"Kelas       : {student['kelas']}")
    print(f"Nilai Tugas : {student['tugas']}")
    print(f"Nilai UTS   : {student['uts']}")
    print(f"Nilai UAS   : {student['uas']}")
    print(f"Rata-rata   : {student['rata_rata']}")
    print(f"Grade       : {student['grade']}")


def edit_student(students):
    print("\n=== EDIT DATA MAHASISWA ===")

    nim = input(
        "Masukkan NIM yang ingin diedit: "
    ).strip()

    student = find_student(
        students,
        nim
    )

    if not student:
        print("[INFO] Data mahasiswa tidak ditemukan.")
        return

    print("\nData saat ini:")
    print(f"Nama  : {student['nama']}")
    print(f"Kelas : {student['kelas']}")
    print(f"Tugas : {student['tugas']}")
    print(f"UTS   : {student['uts']}")
    print(f"UAS   : {student['uas']}")

    nama = input(
        f"\nNama baru [{student['nama']}]: "
    ).strip()

    if nama:
        student["nama"] = nama

    kelas = input(
        f"Kelas baru [{student['kelas']}]: "
    ).strip()

    if kelas:
        student["kelas"] = kelas

    tugas = input_score("Nilai Tugas")
    uts = input_score("Nilai UTS")
    uas = input_score("Nilai UAS")

    average = calculate_average(
        tugas,
        uts,
        uas
    )

    student["tugas"] = f"{tugas:.2f}"
    student["uts"] = f"{uts:.2f}"
    student["uas"] = f"{uas:.2f}"
    student["rata_rata"] = f"{average:.2f}"
    student["grade"] = calculate_grade(average)

    save_students(students)

    print("[SUCCESS] Data berhasil diperbarui.")


def delete_student(students):
    print("\n=== HAPUS DATA MAHASISWA ===")

    nim = input(
        "Masukkan NIM yang ingin dihapus: "
    ).strip()

    student = find_student(
        students,
        nim
    )

    if not student:
        print("[INFO] Data mahasiswa tidak ditemukan.")
        return

    print("\nData yang akan dihapus:")
    print(f"NIM  : {student['nim']}")
    print(f"Nama : {student['nama']}")
    print(f"Kelas: {student['kelas']}")

    confirm = input(
        "\nYakin ingin menghapus data ini? (y/n): "
    ).strip().lower()

    if confirm != "y":
        print("[INFO] Penghapusan dibatalkan.")
        return

    students.remove(student)

    save_students(students)

    print("[SUCCESS] Data mahasiswa berhasil dihapus.")


def ranking_students(students):
    if not students:
        print("\n[INFO] Belum ada data mahasiswa.")
        return

    ranking = sorted(
        students,
        key=lambda student: float(
            student["rata_rata"]
        ),
        reverse=True
    )

    print("\n=== RANKING MAHASISWA ===")

    print("-" * 60)

    for index, student in enumerate(
        ranking,
        start=1
    ):
        print(
            f"{index}. "
            f"{student['nama']} "
            f"({student['nim']}) - "
            f"Rata-rata: {student['rata_rata']} - "
            f"Grade: {student['grade']}"
        )

    print("-" * 60)


def export_csv(students):
    if not students:
        print("\n[INFO] Tidak ada data yang dapat diexport.")
        return

    print("\n=== EXPORT DATA KE CSV ===")
    print("1. Export semua mahasiswa")
    print("2. Export berdasarkan NIM")
    print("3. Export berdasarkan kelas")
    print("4. Kembali")

    choice = input("Pilih menu: ").strip()

    selected_students = []

    if choice == "1":
        selected_students = students.copy()

    elif choice == "2":
        nim = input(
            "Masukkan NIM: "
        ).strip()

        student = find_student(
            students,
            nim
        )

        if not student:
            print(
                "[INFO] Data dengan NIM tersebut "
                "tidak ditemukan."
            )
            return

        selected_students = [student]

    elif choice == "3":
        kelas = input(
            "Masukkan kelas: "
        ).strip()

        selected_students = [
            student
            for student in students
            if student["kelas"].lower()
            == kelas.lower()
        ]

        if not selected_students:
            print(
                "[INFO] Tidak ada mahasiswa "
                "dari kelas tersebut."
            )
            return

    elif choice == "4":
        return

    else:
        print("[ERROR] Pilihan tidak valid.")
        return

    os.makedirs(
        EXPORT_FOLDER,
        exist_ok=True
    )

    filename = input(
        "\nNama file export "
        "(contoh: nilai_mahasiswa.csv): "
    ).strip()

    if not filename:
        print(
            "[ERROR] Nama file tidak boleh kosong."
        )
        return

    if not filename.lower().endswith(".csv"):
        filename += ".csv"

    filepath = os.path.join(
        EXPORT_FOLDER,
        filename
    )

    if os.path.exists(filepath):
        confirm = input(
            f"File '{filepath}' sudah ada. "
            "Timpa? (y/n): "
        ).strip().lower()

        if confirm != "y":
            print("[INFO] Export dibatalkan.")
            return

    try:
        with open(
            filepath,
            mode="w",
            newline="",
            encoding="utf-8-sig"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=FIELDS
            )

            writer.writeheader()
            writer.writerows(
                selected_students
            )

        absolute_path = os.path.abspath(
            filepath
        )

        print(
            f"\n[SUCCESS] "
            f"{len(selected_students)} data berhasil "
            f"diexport."
        )

        print(
            f"[FILE] File tersimpan di:\n"
            f"{absolute_path}"
        )

    except OSError as error:
        print(
            f"[ERROR] Gagal melakukan export: {error}"
        )


def main():
    students = load_students()

    while True:
        print("\n" + "=" * 40)
        print("     STUDENT GRADE MANAGEMENT")
        print("=" * 40)

        print("1. Tambah mahasiswa")
        print("2. Lihat semua mahasiswa")
        print("3. Cari mahasiswa")
        print("4. Edit mahasiswa")
        print("5. Hapus mahasiswa")
        print("6. Ranking mahasiswa")
        print("7. Export data ke CSV")
        print("8. Simpan & Keluar")

        print("=" * 40)

        choice = input(
            "Pilih menu: "
        ).strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            display_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            edit_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            ranking_students(students)

        elif choice == "7":
            export_csv(students)

        elif choice == "8":
            save_students(students)
            print("\nProgram selesai.")
            break

        else:
            print(
                "[ERROR] Pilihan tidak valid. "
                "Silakan pilih 1-8."
            )


if __name__ == "__main__":
    main()