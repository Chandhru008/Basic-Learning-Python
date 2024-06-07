"""
index- 0 1 2 3
lists-[1,2,3,4]
value is the value stored in the list
"""
l=[1,2,3,4,5,6,2,4]

l.remove(2)     # removes by value not by index
print(l)

del l[4]      # deletes by index
print(l)

# removes the value and return the index...removes the value by index 
print(l.pop(3))