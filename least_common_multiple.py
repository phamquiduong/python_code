array = [3,7,2,1,2,8]


def LCM(a,b):
    mul = a*b
    while (a!=b):
        if a>b: a-=b
        else: b-=a
    return mul//a


temp = 1
for value in array:
    temp = LCM(temp, value)

print(temp)
