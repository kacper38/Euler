def largest_palindrome_finder():
    lpp = max([x*y for x in range(100,1000) \
           for y in range(100,1000) \
           if str(x*y) == str(x*y)[::-1]])
    return lpp
