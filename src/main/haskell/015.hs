choose :: Integer -> Integer -> Integer
choose n k = (foldl1 (*) [(k+1)..n]) `div` (foldl1 (*) [1..(n-k)])
