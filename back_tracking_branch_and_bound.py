#*****************************************************************************************
# Đề bài:
#
# You are given positive integers N,M,K, and N positive integers A1,A2,…AN.
# You can choose no more than K elements of A, and let S be the sum of chosen elements.
# Output Yes if it's possible to make S equals to M, and No otherwise.

# Input:
# ___________
# | N M K   |
# | A_1     |
# | A_2     |
# | ..      |
# | A_N     |
# -----------

# Output:
#
# Output Yes if it's possible to make S equals to M, and No otherwise.
#*****************************************************************************************





# Nhận input đầu vào
n, m, k = [int(x) for x in input().split()]
arr = []
for i in range(n):
    arr.append(int(input()))


# Khởi tạo giá trị
ans = False


# Phương pháp quay lui nhánh cận
def back_tracking(i=0, current=-1, sum_1=0):
    global ans
    if ans: return

    for j in range(current+1, n):                   # Tập giá trị nhận được. Giá trị sau luôn lớn hơn giá trị trước đó.
        if ans: return
        sum_1 += arr[j]                             # Ghi nhận giá trị của j
        if sum_1 == m: ans = True
        if sum_1 < m and i < k-1:                   # Nhánh cận -> Nếu tổng nhỏ hơn m và số phần tử chưa vượt quá k thì vẫn còn hi vọng chạy tiếp
            back_tracking(i+1, j, sum_1)            # Chạy cho phần tử tiếp theo
        sum_1 -= arr[j]                             # Khôi phục lại giá trị ghi nhận


# Bắt đầu chạy đệ quy
back_tracking()


# Xuất kết quả
print('Yes' if ans else 'No')
