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