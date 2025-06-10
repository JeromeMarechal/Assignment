

string_1 = "([e]rr)" #false
string_2 = ")([]()" #false
string_3 = "(){[]" #false
string_4 = "(){}[]" #true
string_5 = "(([]))" #true


def valid_parentheses(string):
    bank = [["(", ")"], ["{","}"], ["[", "]"]]
    str_len = len(string)
    count_char = 0
    
    # extra char
    for r in range(len(bank)):
        row = bank[r]
        col_1 = row[0]
        col_2 = row[1]
        
        # set up head and tail in order to check number of char and in which order
        head = 0
        tail = 0
        
        for i in range(len(string)):
            if string[i] == col_1:
                head += 1
            if string[i] == col_2:
                tail += 1
                # check if string start with a close char instead of an open one
                if tail > head:
                    return False
                
        # add number of char to count       
        count_char += (head + tail)
        # check if open char have a close char
        if tail != head:
            return False
        # reset count for next char check
        head = 0
        tail = 0
    # check if there is unvalid char in string
    if count_char == str_len:
        return True    
    else:
        return False        

                
print("String 1:",valid_parentheses(string_1))
print("String 2:",valid_parentheses(string_2))
print("String 3:",valid_parentheses(string_3))
print("String 4:",valid_parentheses(string_4))
print("String 5:",valid_parentheses(string_5))                
            
    
            