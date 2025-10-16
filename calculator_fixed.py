
---

#### 📄 **File 3 (Opsional): `calculator_fixed.py`**  
(Untuk referensi perbaikan — bisa dimasukkan atau tidak)

```python
# calculator_fixed.py
def main():
    print("=== Simple Calculator (Fixed Version) ===")
    try:
        num1 = float(input("Masukkan angka pertama: "))
        num2 = float(input("Masukkan angka kedua: "))
    except ValueError:
        print("❌ Error: Input harus berupa angka!")
        return

    op = input("Operator (+, -, *, /): ").strip()

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("❌ Error: Tidak bisa membagi dengan nol!")
            return
        result = num1 / num2
    else:
        print("❌ Error: Operator tidak valid! Gunakan +, -, *, atau /")
        return

    print("✅ Hasil:", result)

if __name__ == "__main__":
    main()