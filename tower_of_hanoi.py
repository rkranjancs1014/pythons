#question 14
def tower_of_hanoi(n, from_peg, to_peg, aux_peg):
    if n == 1:
        print("move dick 1 from ", from_peg , " to ", to_peg)
        return
    else:
        tower_of_hanoi(n-1, from_peg, aux_peg, to_peg)
        print("move dick", n ,"from " , from_peg, " to", to_peg)
        tower_of_hanoi(n-1, aux_peg, to_peg, from_peg)
