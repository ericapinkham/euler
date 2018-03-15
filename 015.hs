factorial :: Int -> Int
factorial n = foldl1 (*) [1..n]

choose :: Int -> Int -> Int
choose n k = (factorial n) `div` (factorial (n - k) * factorial k)
