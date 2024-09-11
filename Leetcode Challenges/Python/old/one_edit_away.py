"""Given two strings, write a function to check if they are one edit (or zero edits) away"""

def one_edit_away(first, second):
    if len(first) == len(second):
        return one_edit_replace(first, second)
    elif (len(first) + 1) == len(second):
        return one_edit_insert(first, second)
    elif (len(first) -1) == len(second):
        return one_edit_insert(second, first)

def one_edit_replace(first, second):
    found_diff = False
    for i in range(len(first)):
        if first[i] != second[i]:
            if found_diff: # if has already found difference, then strings are not oneeditreplace
                return False
            found_diff = True
    return True

def one_edit_insert(first, second):
    index1 = 0
    index2 = 0

    while (index2 < len(second) and index1 < len(first)):
        if first[index1] != second[index2]:
            if (index1 != index2):
                return False
            index2 += 1 
        else:
            index1 += 1
            index2 += 1
        
        return True



if __name__ == '__main__':
    a = "pale"
    b = "bae"
    print(one_edit_away(a, b))