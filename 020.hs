sumDigits :: Int
sumDigits = sum $ map (\x -> ord x - 48) $ show $ foldl1 (*) [1..100]
