n = int(input())
list1 = []
for i in range(n):
    list1.append(int(input()))
list2 = sorted(list1)
for i in range(n):
    print(list2[i])
