x = float(input("Nhập vào 1 số: "))

m = None
if x > 0:
    m = "số dương"
elif x < 0:
    m = "số âm"
else:
    m = "số 0"

print(f"x là {m}")
