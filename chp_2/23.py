# Changing the value of 'a' creates a NEW object in memory, resulting in a different ID.
lst = [1, 2, 3]
a = 10
# Checking IDs
print(id(a))
# Updating Immutable
a = 20
print(id(a))
# Updating Mutable
print(id(lst))
lst[1] = 12
print(id(lst))
