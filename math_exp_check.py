def exp_matching(exp):
    left = '({['
    right = ')}]'
    S = ArrayStack()
    for ch in exp:
        if ch in left:
            S.push(ch)
        elif ch in right:
            if S.is_empty():
                return False
            if right.index(ch) != left.index(S.pop()):
                return False
    return S.is_empty()
