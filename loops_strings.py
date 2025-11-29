def count_vowels(str: str)->int:
    vowels = ["a","e","i","o","u"]
    count_vowels = 0
    for i in range(0,len(str),1):
        for k in range(0,len(vowels)):
            if(str[i].lower() == vowels[k]):
                count_vowels += 1
    return count_vowels

def Longest_Word(str_ :str)->str:
    longest_word = ""
    index = 0
    while index < len(str_):
        count = index
        new_str = ""
        while count < len(str_) and (str_[count].isalpha()):
            new_str += str_[count]
            count += 1
            index = count -1
        if(len(new_str) > len(longest_word)):
            longest_word = new_str
        index += 1
    return longest_word

def CapOnFirst(str_ :str):
    index = 0
    while index < len(str_):
        count = index 
        char_first = index 
        while count < len(str_) and (str_[count].isalpha()):
            if(count == char_first):
                str_.insert
                str_.pop(count)
            count += 1
            index = count 
        index += 1
    return str_
            
word = input("ENTER SENTENCE = ")
print(f"SENTENCE IN CAMILE CASE [{CapOnFirst(word)}]")
    