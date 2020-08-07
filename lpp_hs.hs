

w1 = [ x | y <- [100..999], z <-[y..999], let x=y*z]
lpp = maximum [ x | x <- w1, let c = show x, c == reverse c ]

-- as one 
lpp_finder = maximum [ x | y <- [100..999], z <- [y..999], let x=y*z,let s = show x, s == reverse s ]
