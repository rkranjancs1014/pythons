def html_tag_check(row):
    S = ArrayStack()
    j = row.find('<')
    while j != -1:
        k = row.find('>', j+1)
        if k == -1:
            return False
        tag = row[j+1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = row.find('<', k+1)
    return S.is_empty()
                
