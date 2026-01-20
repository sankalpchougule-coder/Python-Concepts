# CORE PYTHON FUNCTIONS (must-know)

# 1. print()
# Dispaly output to console

print("Hello",name)

# 2. len
# Find length of strings, lists, tuples, dicts

len([1,2,3])

# 3. type()
# Check datatype

type(3.14)

# 4. input()
# Take input from user

name = input("Enter name:")

# 5. id()\
# Get memory location of object.



# LIST & SEQUENCE FUNCTIONS

# 6. range()
# used in loops

for i in range(10):
    print(i)


# 7. enumerate()
# Iterate with index + item

for idx, val in enumerate(['a','b']):
    print(idx,val)


# 8. zip()
# Combine multiple iterables

for x,y in zip([1,2],[3,4]):
    print(x,y)

# 9. Sorted()
# Returns in reverse

for i in reversed("abcd"):
    print(i)


# USEFUL BUILT-INS

# 11. map()
