# Chương trình nhập hai số và tính tổng

# Bước 1: Nhập dữ liệu từ bàn phím
# Hàm input() trả về kiểu chuỗi (string), nên ta cần ép kiểu sang float để tính toán
a = float(input("Nhập số thứ nhất (a): "))
b = float(input("Nhập số thứ hai (b): "))

# Bước 2: Thực hiện phép cộng
tong = a + b

# Bước 3: In kết quả ra màn hình
print(f"Kết quả của phép cộng {a} + {b} là: {tong}")