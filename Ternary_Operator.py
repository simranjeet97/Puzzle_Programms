def TernaryOperator(a, b, c):

# If a is true, we return
# (1 * b) + (!1 * c) i.e. b
# If a is false, we return
# (!1 * b) + (1 * c) i.e. c

    return ((not not a) * b + (not a) * c)

a = 100
b = 10
c = 20

# Function call to output b or c
# depending on a
print(TernaryOperator(a>b, b, c))

a = 0

# Function call to output b or c
# depending on a
print(TernaryOperator(a>b, b, c))
