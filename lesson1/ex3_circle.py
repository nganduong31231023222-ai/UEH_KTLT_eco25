# ex3_circle.py
import math

# nhập bán kính từ người dùng
r = float(input("Nhập bán kính hình tròn: "))

# tính chu vi và diện tích
cv = 2 * math.pi * r
dt = math.pi * r**2

# in kết quả
print(f"Chu vi hình tròn: {cv:.2f}")
print(f"Diện tích hình tròn: {dt:.2f}")
