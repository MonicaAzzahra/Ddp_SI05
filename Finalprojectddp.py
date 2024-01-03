import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

def calculate_ratio():
    try:
        harga_satuan = float(entry_harga_satuan.get())
        jumlah_produk = int(entry_jumlah_produk.get())
        biaya = float(entry_biaya.get())

        # Pendapatan
        pendapatan = harga_satuan * jumlah_produk

        # Revenue cost ratio
        ratio_pct = pendapatan / biaya

        # Benefit cost ratio
        benefit = pendapatan - biaya
        benefit_cost_ratio = benefit / biaya

        # Hasil pada label
        result_text = f"Revenue Cost Ratio: {ratio_pct:.2f}\nBenefit Cost Ratio: {benefit_cost_ratio:.2f}"

        # Result akhir
        if ratio_pct > 1.3 and benefit_cost_ratio > 0:
            result_text += "\nUsaha Layak untuk dikembangkan"
        elif ratio_pct <= 1.3 and benefit_cost_ratio <= 0:
            result_text += "\nUsaha Tidak Layak untuk dikembangkan"
        else:
            result_text += "\nPenilaian Usaha Belum Jelas"

        result_label.config(text=result_text)

    except ValueError:
        result_label.config(text="Masukkan nilai yang valid.")


root = tk.Tk()
root.title("Aplikasi Analisa Kelayakan Usaha")

style = Style("vapor")
style.configure("TLabel", padding=5)

frame = ttk.Frame(root, padding="500 200 200 300")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="KELAYAKAN USAHAKU", font=("Helvetica", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

ttk.Label(frame, text="Harga Satuan:").grid(row=1, column=0, sticky=tk.W)
entry_harga_satuan = ttk.Entry(frame)
entry_harga_satuan.grid(row=1, pady=10, column=1, sticky=tk.W)

ttk.Label(frame, text="Jumlah Produk:").grid(row=2, column=0, sticky=tk.W)
entry_jumlah_produk = ttk.Entry(frame)
entry_jumlah_produk.grid(row=2, pady=10, column=1, sticky=tk.W)

ttk.Label(frame, text="Biaya:").grid(row=3, column=0, sticky=tk.W)
entry_biaya = ttk.Entry(frame)
entry_biaya.grid(row=3, column=1, pady=10, sticky=tk.W)

calculate_button = ttk.Button(frame, text="Hitung Rasio", command=calculate_ratio)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

result_label = ttk.Label(frame, text="")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
