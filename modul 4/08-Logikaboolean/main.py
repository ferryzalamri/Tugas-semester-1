# operasi logika atau boolean

#not, or, and

#NOT
print("===NOT===")
a = False
c = not a
print("data a = ", a)
print("-------------------NOT")
print("data c = ", c)

# OR (jika salah satu true, hasilnya akan true)
print("====OR====")
a = False
b = False
c = a or b
print(a, "OR", b, "=", c)
a = True
b = False
c = a or b
print(a, "OR", b, "=", c)
a = False
b = True
c = a or b
print(a, "OR", b, "=", c)
a = True
b = True
c = a or b
print(a, "OR", b, "=", c)

# AND 
print("====AND====")
a = False
b = False
c = a and b
print(a, "and", b, "=", c)

a = True
b = False
c = a and b
print(a, "and", b, "=", c)

a = False
b = True
c = a and b
print(a, "and", b, "=", c)

a = True
b = True
c = a and b
print(a, "and", b, "=", c)