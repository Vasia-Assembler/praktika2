import random
n = 4
max_random = 10000000
integer_set = set()
real_set = set()

for x in range(0, n):
    real_set.add(random.uniform(float(-max_random), float(max_random)))
    integer_set.add(random.randint(-max_random, max_random))
if (integer_set.issubset(real_set)) or (real_set.issubset((integer_set))):
    print("")
else:
    print(integer_set.intersection(real_set))
    print(integer_set.union(real_set))
    print(integer_set.difference(real_set))
    print(real_set.difference(integer_set))