alphanum="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
prec = {}
prec["*"] = 3
prec["/"] = 3
prec["+"] = 2
prec["-"] = 2
prec["("] = 1
def infix_to_postfix(exp):
    output_list = []
    operator_Stack = ArrayStack()
    left_parentheses = "[{("
    right_parentheses = ")}]"
    for char in exp:
        if ord(char) != 32:
            if char in alphanum:
                output_list.append(char)
            elif char in left_parentheses:
                operator_Stack.push(char)
            elif char in right_parentheses:
                if not operator_Stack.is_empty():
                    pop_ele = operator_Stack.pop()
                    while pop_ele not in left_parentheses:
                        output_list.append(pop_ele)
                        pop_ele = operator_Stack.pop()
            else:
                while(not operator_Stack.is_empty()) and (prec[operator_Stack.top()] >= prec[char]) :
                    pop_ele = operator_Stack.pop()
                    output_list.append(pop_ele)
                operator_Stack.push(char)
    while not operator_Stack.is_empty():
        output_list.append(operator_Stack.pop())
    return ' '.join(output_list)
                
            
        
