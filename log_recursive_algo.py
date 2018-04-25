# find log using recursion
def integral_log_base_2(n):
    number_of_2 = 0
    if n < 2:
        return 0 
    else:
         return 1+integral_log_base_2(n/2)
