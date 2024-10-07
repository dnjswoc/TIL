# add
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.add(4)
print(my_set)

my_set.add(4)
print(my_set)

# clear
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.clear()
print(my_set)  # set()

# remove
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.remove(2)
print(my_set)
# my_set.remove(10)  # KeyError: 10

# pop
my_set = {'a', 'b', 'c', 1, 2, 3}
element = my_set.pop()
print(element)

# discard
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.discard(2)
print(my_set)
my_set.discard(10)

# update
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.update([1, 4, 5])
print(my_set)  # {1, 'a', 3, 2, 'c', 4, 5, 'b'}

# 집합 메서드
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

print(set1.difference(set2))  # {0, 2, 4}
print(set1.intersection(set2))  # {1, 3}
print(set1.issubset(set2))  # False
print(set3.issubset(set1))  # True
print(set1.issuperset(set2))  # False
print(set1.union(set2))  # {0, 1, 2, 3, 4, 5, 7, 9} 
