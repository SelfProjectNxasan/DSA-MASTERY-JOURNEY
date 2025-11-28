def remove_char_str(str_word, str_char_):
    new_str = ""
    for i in range(0,len(str_word)):
     if str(str_word[i]) != str_char_:
        new_str += str_word[i]
    return new_str

def Sum_Digits(word :str):
   sum = 0
   for i in range(0,len(word)):
      if (word[i].isdigit()):
         sum += int(word[i])
   return sum

def Insert_Index(word :str,str_targ :str,index_ :int):
   str_new = word[0:(index_):] + str_targ + word[(index_):len(word)]
   return str_new

def Remove_Char_Index(input_str: str, index_ :int):
   return input_str[:index_:] + input_str[index_+1::]

def ReplaceCharAtIndex(str_ :str, index_old :int,index_new:int):
   temp_var = index_new
   if index_old > index_new:
      index_new,index_old = index_old,temp_var
      new_str = str_[:index_old:]+str_[index_new]+str_[index_old+1:index_new:]+str_[index_old]+str_[index_new+1::]
   return new_str

def Truncate_Empty_Space(str_ :str)->str:
   new_str = str_.strip(' ')
   new_str_ = ""
   index = 0
   while index < len(new_str):
      inner_index = index
      while new_str[inner_index].isspace() and inner_index < len(new_str):
        inner_index += 1
      if (inner_index > index and (inner_index-index) > 1):
         index = inner_index
      else:
         new_str_ += new_str[index]
      index+=1
   return new_str_
      
def count_substring_occur(str_ :str, sub_str :str)->int:
   i = 0
   sum_sub_str = 0
   while (i+len(sub_str)) <= len(str_):
      if str_[i:(i+len(sub_str)):] == sub_str:
         sum_sub_str+= 1
      i +=1
   return sum_sub_str

word = input("Enter a Word = ")
sub_string = input("Enter a substring = ")
substring_count = count_substring_occur(word,sub_string)
print(f" SUBSTRING [{sub_string}]   OCCURED  [{substring_count}]  @WORD [{word}]")



