sumDigits :: Int
sumDigits = sum $ map (\x -> ord x - 48) $ show $ 2 ^ 1000
