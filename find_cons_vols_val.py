#Use recursion to write a Python function for determining if a string s has
more vowels than consonants.
def question_18(s, c=0, v=0):
    vowels = 'aeiou'
    if len(s) == 0:
        if v > c:
            return True
        else:
            return False
    elif s[0] in vowels:
        v = v+1
        return question_18(s[1:], c, v)
    else:
        c = c+1
        return question_18(s[1:], c, v)
