#Ý 1 câu Q1:

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print("")

#Ý 2 câu Q1:

n = int(input("Enter number "))
sum = 0
for i in range(1,n+1):
    sum = sum + i
print("Sum is: ",sum)