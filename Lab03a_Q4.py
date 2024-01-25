#Ý 1 câu Q4:

str1 = 'I am 25 years and 10 months old'

for i in str1:
    if i in '0123456789':
        print(i, end='')

#Print để tách dòng ý 1 và ý 2
print("")
#Ý 2 câu Q4:

str1 = "/*Jon is @developer & musician"

def remove_special_symbols(input_string):
    new_str = ""
    for char in input_string:
        if char not in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~":
            new_str += char
    return new_str

new_str = remove_special_symbols(str1)
print(new_str)

#Ý 3 câu Q4:

str_list = ['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']

print("Original list of string")
print(str_list)
print("")

for i in str_list:
    if i == "" or i == None:
        str_list.remove(i)

print("After removing empty strings")
print(str_list)

#Ý 4 câu Q4:

str1 = 'Emma-is-a-data-scientist'
f = str1.split(sep="-")
for i in f:
    print(i)