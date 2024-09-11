set1 = {8, 16, 24, 32, 44}
set2 = {7, 14, 8, 32, 21}

difference_set = set1 - set2
print(difference_set)
difference_set = set2 - set1
print(difference_set)

union_set = set1 | set2
print(union_set)

symdiff_set = set2 ^ set1
print(symdiff_set)
symdiff_set = set1 ^ set2
print(symdiff_set)

intersection_set = set1 & set2
print(intersection_set)
intersection_set = set2 & set1
print(intersection_set)