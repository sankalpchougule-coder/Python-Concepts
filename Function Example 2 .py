# Sqaure of no

def square(num):
    return num * num

result = square(12)
print("Square:", result)


# Cube of no

def cube(a):
    return a * a * a

result = cube(5)
print("Cube:",result)


# Even and odd

def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
number = int(input("Enter a number: "))
result = even_odd(number)
print(result)


