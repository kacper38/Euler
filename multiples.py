'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def multiples(z):
    ''' finds all natural numbers below 10 that are multiples
    of 3 or 5, (not 0!), and returns their sum
    
    input: z -> right limit of search (s.open)
    '''
    c=0
    for x in range (1,z):
        if x % 3 == 0 or x % 5 ==0:
            c+=x
    return c
