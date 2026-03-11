def sum(a,b):
    return a + b
if __name__ == "__main__":
    a = float(input("Nhập số thứ nhất (a): "))
    b = float(input("Nhập số thứ hai (b): "))
    tong = sum(a, b)
    print(f"Kết quả của phép cộng {a} + {b} là: {tong}")