# calculator.py
# Simple Calculator with intentional defects for RCA assignment

def main():
    print("=== Simple Calculator (Defect Version) ===")
    num1 = input("Masukkan angka pertama: ")
    num2 = input("Masukkan angka kedua: ")
    op = input("Operator (+, -, *, /): ")

    if op == "+":
        result = num1 + num2  # ❌ DEFECT 1: String concatenation
    elif op == "-":
        result = num1 - num2  # ❌ TypeError: unsupported operand
    elif op == "*":
        result = num1 * num2  # ❌ TypeError or weird string repeat
    elif op == "/":
        result = num1 / num2  # ❌ TypeError + no zero check
    else:
        result = "Hasil tidak dapat dihitung."  # ❌ DEFECT 3: Silent failure

    print("Hasil:", result)

if __name__ == "__main__":
    main()