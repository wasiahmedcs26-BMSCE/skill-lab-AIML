
# Positional Arguments

# def info(name,age):
#     print(f"I am {name} and I am {age} years old")

# info ("Vedavathi",16)
# info ("Meenakshi",19)

# # Keyword arguments

# def info(name,age):
#     print(f"I am {name} and I am {age} years old")

# info(age=20,name="Vijay")

# # Default Argument

# def info(age,name="XYZ"):
#     print(f"I am {name} and I am {age} years old")

# info(20,"Ravi")
# info(20)

# Variable number of arguments

def total_bill(*args):
    sum=0
    for x in args:
        sum+=x
    return sum
print(total_bill(1500,2800))
print(total_bill(1800))
print(total_bill())
