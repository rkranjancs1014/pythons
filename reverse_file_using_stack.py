def reverse_a_file(filename):
    """overwrite a file in reverse order"""
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstripe('\n'))
    original.close()
    output = open(filename, 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()
