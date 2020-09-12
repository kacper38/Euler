"""
Created on Fri Sep 11 15:14:20 2020

@author: kacper
"""
  
        
def prime_check(x):
    divo = range(2, int(x**.5) + 1)
    for i in divo:
        if x % i == 0:
            return False
    return True

        
def n_th_prime(n_th):
    n = 2
    no_prime = 1
    while no_prime < n_th:
        n+=1
        if prime_check(n):
            no_prime+= 1
    return n
    

print(n_th_prime(10001))
