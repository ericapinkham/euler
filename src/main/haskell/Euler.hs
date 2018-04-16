module Euler
( divisors,
  choose
) where

divisors :: Int -> [Int]
divisors n = foldl (\acc x -> if n `quot` x == x then x:acc else x:(n `quot` x):acc) [] $ filter (\x -> n `mod` x == 0) $ takeWhile (< (roundupsqrt n)) [1..]
    where roundupsqrt x = ceiling (sqrt (fromIntegral x))

choose :: Integer -> Integer -> Integer
choose n k
  | n == k = 1
  | k == 0 = 1
  | k > n = error "k exceeds n"
  | otherwise = (foldl1 (*) [(k+1)..n]) `div` (foldl1 (*) [1..(n-k)])
