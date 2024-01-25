#Ý 1 câu Q3:

def middle_four_chars(string):
    length = len(string)
    if length < 4:
        return string
    
    if length % 2 == 0:
        start_index = (length - 3) // 2
    else:
        start_index = length // 2 - 1

    result = ""
    for i in range(4):
        result += string[start_index + i]

    return result

string = input("Original String is ")
print("Middle four chars are: ",middle_four_chars(string))

#Ý 2 câu Q3:

def insertString(s1, s2): 
    return s1[:len(s1)//2] + s2 + s1[len(s1)//2:]

s1 = "Ault" 
s2 = "Kelly" 
s3 = insertString(s1, s2) 
print(s3)

#Ý 3 câu Q3:
s1 = "America" 
s2 = "Japan" 

def f(s1, s2): 
    return s1[0] + s2[0] + s1[int(len(s1) / 2)] + s2[int(len(s2) / 2)] + s1[-1] + s2[-1]

result = f(s1, s2) 
print(result)

#Ý 4 câu Q3:

str1 = "PyNaTive"
str2 = ""
str3 = ""

for i in range(len(str1)):
    if "a" <= str1[i] <= "z":
        str2 = str2 + str1[i]
    if "A" <= str1[i] <= "Z":
        str3 = str3 + str1[i]

print(str2+str3)

#Ý 5 câu Q3:

str = input("Input string= ")

NumberOfLetters = 0
NumberOfDigits = 0
NumberOfOther = 0

for i in range (len(str)):
    if '0' <= str[i] and str[i] <= '9':
        NumberOfDigits += 1
    elif ('a' <= str[i] and str[i] <='z') or ('A' <= str[i] and str[i] <= "Z"):
        NumberOfLetters += 1
    else:
        NumberOfOther += 1

print("total counts of chars, Digits, and symbols")
print("")
print("Char = ",NumberOfLetters," Digits = ", NumberOfDigits," Symbol = ", NumberOfOther)