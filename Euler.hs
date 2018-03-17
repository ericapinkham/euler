module Euler
( divisors
) where

divisors :: Int -> [Int]
divisors n = foldl (\acc x -> if n `quot` x == x then x:acc else x:(n `quot` x):acc) [] $ filter (\x -> n `mod` x == 0) $ takeWhile (< (roundupsqrt n)) [1..]
    where roundupsqrt x = ceiling (sqrt (fromIntegral x))
