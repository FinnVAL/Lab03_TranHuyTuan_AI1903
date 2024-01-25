def anagram_test(word1, word2):
    return sorted(word1) == sorted(word2)

def input_check(prompt):
    while True:
        word = input(prompt)
        if word.isalpha():
            return word
        else:
            print("Hãy nhập vào một từ!")

def result():
    word1 = input_check("Nhập vào từ đầu tiên: ")
    word2 = input_check("Nhập vào từ thứ hai: ")

    if anagram_test(word1, word2):
        print("Hai từ này là anagrams.")
    else:
        print("Hai từ này không phải anagrams.")

result()