#Ý 1 câu Q2:

f = input("Nhập vào 1 dãy số: ")
n = f.split()
for i in n:
    x = int(i)
    if x%5 == 0: 
        if x <= 150:
            print(x)
            continue
        if x > 500:
            break

#Ý 2 câu Q2:
a = int(input("Nhập vào 1 số: "))
b = a
count = 0
while b > 0:
    b = b // 10
    count = count + 1
print("Số ",a," có ",count," chữ số.")

#Ý 3 câu Q2:

list1 = input("Nhập vào 1 dãy số :").split()
t = len(list1) - 1
while t >= 0:
    print(list1[t])
    t -= 1