import tkinter as tk
top = tk.Tk()

top.title("Aplikasi Prediksi Prodi Pilihan")
top.geometry("380x540")
top.configure(bg="#25255c")

judul = tk.Label(top, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16, "bold"), bg="#25255c", fg="white")
judul.pack(pady=20)
frame = tk.Frame(top, bg="#25255c")
frame.pack(pady=5)
nilai = []

for i in range(10):
    label = tk.Label(frame, text="Nilai Mata Pelajaran " + str(i+1) + ":", bg="#25255c", fg="white", width=22, anchor="w")
    label.grid(row=i, column=0, padx=5, pady=4)

    entry = tk.Entry(frame, width=12)
    entry.grid(row=i, column=1, padx=5, pady=4)
    nilai.append(entry)

jurusan = tk.Label(top, text="Masukkan Jurusan Anda:", bg="#25255c", fg="white")
jurusan.pack(pady=(15, 3))

daftar_jurusan = ["Teknologi Informasi", "Teknik Mesin", "Teknik Sipil", "Teknik Elektro"]