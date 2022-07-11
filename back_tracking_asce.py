def check(s):
    print(s)


def back_tracking(i=0, current=-1):
    for j in range(current+1, n):
        s[i] = j                        # Ghi nhận giá trị j
        if i >= k-1:                    # Nếu đủ k phần tử thì kiểm tra
            check(s)
        else:
            back_tracking(i+1, j)       # Gọi đệ quy cho phần tử tiếp theo


# Đầu vào
n = 3               # Giá trị được nhận
k = 2               # Số phần tử
s = [0]*k           # Khởi tạo mảng lưu giá trị được nhận

back_tracking()     # Gọi quay lui
