def add(a, b):
    print "ADDING ", a, " + ", b
    c = a + b
    return c

def subtract(a, b):
    print "SUBTRACTING ", a, " - ", b
    c = a - b
    return c

def multiply(a, b):
    print "MULTIPLYING ", a, " * ", b
    c = a * b
    return c

def divide(a, b):
    print "DIVIDING ", a, " / ", b
    c = a / b
    return c

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "age: ", age
print "height: ", height
print "weight: ", weight
print "iq: ", iq

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"