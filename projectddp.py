import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

def calculate_ratio():
    try:
        # Ambil nilai dari input
        harga_satuan = float(entry_harga_satuan.get())
        jumlah_produk = int(entry_jumlah_produk.get())
        biaya = float(entry_biaya.get())

        # Hitung pendapatan
        pendapatan = harga_satuan * jumlah_produk

        # Hitung rasio pendapatan terhadap biaya
        ratio_pct = pendapatan / biaya

        # Hitung benefit cost ratio
        benefit = pendapatan - biaya
        benefit_cost_ratio = benefit / biaya

        # Tampilkan hasil pada label
        result_label.config(text=f"Revenue Cost Ratio: {ratio_pct:.2f}\n"
                                f"Benefit Cost Ratio: {benefit_cost_ratio:.2f}")
    except ValueError:
        result_label.config(text="Masukkan nilai yang valid.")

# Buat instance dari tkinter
root = tk.Tk()
root.title("Revenue Cost Ratio Calculator")

# Gaya menggunakan ttkbootstrap
style = Style("cyborg")
style.configure("TLabel", padding=5)

# Buat dan atur widget
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Harga Satuan:").grid(row=0, column=0, sticky=tk.W)
entry_harga_satuan = ttk.Entry(frame)
entry_harga_satuan.grid(row=0, column=1, sticky=tk.W)

ttk.Label(frame, text="Jumlah Produk:").grid(row=1, column=0, sticky=tk.W)
entry_jumlah_produk = ttk.Entry(frame)
entry_jumlah_produk.grid(row=1, column=1, sticky=tk.W)

ttk.Label(frame, text="Biaya:").grid(row=2, column=0, sticky=tk.W)
entry_biaya = ttk.Entry(frame)
entry_biaya.grid(row=2, column=1, sticky=tk.W)

calculate_button = ttk.Button(frame, text="Hitung Rasio", command=calculate_ratio)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = ttk.Label(frame, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Jalankan aplikasi
root.mainloop()
