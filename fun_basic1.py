
# 5  /one 
def a():
    return 5
print(a()) 


#5,10  /two
def a():
    return 5
print(a()+a())


#5,10,5  /three
def a():
    return 5
    return 10
print(a())


# 5,10,5,5  /four
def a():
    return 5
    print(10)
print(a())


# 5, none / a() was never returned   / five
def a():
    print(5)
x = a()
print(x)


# 3,5, none / type error  /six
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))


#25 /seven
def a(b,c):
    return str(b)+str(c)
print(a(2,5))


# 100, 10 /eight
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())


# 7,14,21 /nine
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))


#8  /ten 
def a(b,c):
    return b+c
    return 10
print(a(3,5))


#500,300,500,300 /eleven
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)


#500,300,500,500 / twelve 
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)


# 500,500,300,300 / thirteen
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)


# 1,2,3,1,2 CONFUSED / fourteen
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()


#  1,3,5,10 / fifteen
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)