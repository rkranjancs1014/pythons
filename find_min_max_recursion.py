#find min max using recursion
def find_min_max(seq, left, right):
    if len(seq) == 0:
        return
    if left + 1 > right :
        if seq[left] < seq[right]:
            return seq[left], seq[right]
        else:
            return seq[right],seq[left]
        
    mid = (left + right) // 2
    (left_min, left_max) = find_min_max(seq, left, mid)
    (right_min, right_max) = find_min_max(seq, mid + 1, right)
    
    max_value = left_max
    min_value = left_min
    if right_max > max_value:
        max_value = right_max
    if right_min < min_value:
        min_value = right_min
    return min_value, max_value
