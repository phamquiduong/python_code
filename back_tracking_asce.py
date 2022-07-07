# Have n value. Get k item.


def check(s):
    print(s)


def back_tracking(i, current, n, k, s, b):
    for j in range(current, n+1):
        if b[j]:
            s[i] = j
            if i >= k-1:
                check(s)
            else:
                b[j] = False    # Remove if item select can same them
                back_tracking(i+1, j, n, k, s, b)
                b[j] = True


n = 4
k = 2
s = [0]*k
b = [True]*(n+1)

back_tracking(0, 0, n, k, s, b)
