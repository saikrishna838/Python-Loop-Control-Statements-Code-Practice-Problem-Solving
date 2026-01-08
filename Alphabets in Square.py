n = int(input())
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(n):
    for j in range(n):
        print(s[j], end= " ")
    print()