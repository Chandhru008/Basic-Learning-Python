# Dictionary
# {}
# not iterable i.e no enumerated(one by one) index
#dictionaries are hashed    |md5
"""
creating an empty dict:- d={}
                        d=dict()
creating a dict with data :-  d={"key":"value"}

key must be a immutable data type
1)int
2)float
3)string
4)other immutable data types

"""
d={"hello":"world"}
print(type(d))

print(d["hello"])   #if input as hello prints world

f={(1,2,3):"tuple"}
print(f[(1,2,3)])    # displays as tuple
