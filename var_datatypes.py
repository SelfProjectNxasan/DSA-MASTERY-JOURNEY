
def sum_two_nums(a :int,b :int):
    sum = a+b
    print(f"{a} + {b} = {sum}")

def even_odd(a :int) -> bool:
    if(a % 2 == 0):
        return True
    else:
        return False
    
def convert_to_ferheit(celcius_input :float)->float:
    retrun_ferheit = (celcius_input *(9/5))+32
    return retrun_ferheit

def calc_interest(principal: float) ->float:
    return (principal*20*2)/100

def reverse_string(str_ :str)->str:
    return str_[::-1]

def reverse_str(str_: str)->str:
    reversed_ = ""
    for i in range(len(str_)-1,-1,-1):
        reversed_ += str_[i]
    return reversed_

def word_count_beta(sentence:str)->int:
    all_words = sentence.strip(" ").split(" ")
    return len(all_words)

def alpha_word_count(str:str)->int:
    all_words = []
    found_char = False
    index = 0
    while index < len(str):
        if(str[index].isalpha()):
            new_word = ""
            found_char = True
            print(f"INDEX ENTERED {index}")
            count = index 
            while found_char:
                if(str[count].isalpha() == False):
                    all_words.append(new_word)
                    index = count - 1
                    found_char = False
                    print(f"INDEX TO EXIT {index} / {len(str)}")
                else:
                    new_word += str[count]
                count += 1
        index += 1
    return len(all_words)


a = input("ENTER SENTENCE = ")
print(f"WORD COUNT =  [{alpha_word_count(a)}]")