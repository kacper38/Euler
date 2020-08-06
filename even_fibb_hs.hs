even_fibb_terms =sum [ x | x <- takeWhile(<=4000000) fib, even x]
    where
	fib = 1 : scanl (+) 0 fib
