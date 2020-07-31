"
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

Naive approach
"


def find_fibb_even_terms_sum(x):
    fibd = [1,2]
    even_terms = 0

    while fibd[1] < x:
        if fibd[1]%2 == 0:
            even_terms +=fibd[1]
        t = fibd[1]    
        fibd[1] = fibd[0] + fibd[1]
        fibd[0] = t
    return (even_terms)
