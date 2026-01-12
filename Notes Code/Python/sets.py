nums = {1,2,3,4,5,5}
print(nums)
print(type(nums))

print(len(nums))

# EMPTY Sets

num = set()

# Meathods add, remove, clear, pop


nums.add(100)
print(nums)
nums.remove(100)
print(nums)
print(nums.pop())
nums.clear()
print(len(nums))

# Union

set1 = {1,1,2,2,3,3,4,5}
set2 = {6,7,7,8,9,9}
set3 = set1.union(set2)
print(set3)

#intersection

set4 = set1.intersection(set2)
print(set4)