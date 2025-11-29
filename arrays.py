import str_add_modify as str


def findTarget(array_input: list, target):
    isFound = False
    if type(target) != type(array_input[0]):
        print(f"TRAGET TYPE IS {type(target)}  WHEILE ELEMENT IS {type(array_input[0])}")
        return False
    for k in range(0,len(array_input)):
        if(array_input[k] == target):
            isFound = True
            break
    return isFound
def Replace(input_array:list,old_val,new_val)->list:
    for i in range(0,len(input_array)):
        if(input_array[i] == old_val):
            input_array[i] = new_val
    return input_array
def AddItem(ar:list,item_add)->list:
    ar.append(item_add)
    return ar
def RemoveItem(a:list,item)->list:
    ret = []
    for i in range(0,len(a)):
        if a[i] != item:
            ret.append(a[i])
    return ret
def get_odd(ar:list)->list:
    return [x for x in ar if x % 2 != 0]

    return [x for x in ar if x % 2 != 0]
elements = [57,8,9,4,8,4,8,44,3]
is_five = get_odd(elements)
print(f"ODD NUMBERS = [{is_five}]")