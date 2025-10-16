# Simple Calculator (Defect Version)

Mini program kalkulator sederhana dengan **3 defect sengaja** untuk tugas Root Cause Analysis (RCA).

## 🐞 Defect yang Ada
1. **Input tidak dikonversi ke angka** → operasi dilakukan pada string (misal: "2" + "3" = "23")
2. **Tidak ada penanganan pembagian dengan nol** → crash jika membagi dengan 0
3. **Tidak ada validasi operator** → input seperti `%`, `abc`, atau kosong tidak ditangani

## ▶️ Cara Menjalankan
```bash
python calculator.py