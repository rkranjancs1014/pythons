def exp_check(string):
    left = '{'
    right = '}'
    p = []
    entry = 0
    for i in string:
        if i == left:  
            if len(p)>1:
                if p[-1] == right:
                    p.pop()
                    p.pop()
                    entry += 1
            p.append(i)
        elif i == right:
            if len(p) >= 1:
                if p[-1] == left:
                    p.append(i)
                elif p[-1] == right:
                    if len(p) >= 2:
                        if p[-2] == right:
                            entry +=1
                            p.pop()
                            p.pop()
                            p.append(i)
                        elif p[-2] == left:
                            p.pop()
                            p.pop()
                    else:
                        p.append(i)
            else:
                p.append(i)
    right_counter = 0
    for i in range(len(p)):
        v = p.pop()
        if v == right:
            right_counter += 1
        elif v == left and right_counter == 1:
            entry += 1
            right_counter = 0
        elif v == left and right_counter ==0:
            entry += 2
    if right_counter == 2:
        entry +=1
    if right_counter == 1:
        entry += 2
    return entry
    
    
if __name__ == "__main__":
    print(check_exp('{{}}}}'))
