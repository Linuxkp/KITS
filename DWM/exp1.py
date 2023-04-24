#program 1

list1 = ['physics','chemistry',1997,2000]
list2 = [1,2,3,4,5,6,]
print("list1[0]:",list1[0])
print("list2[1:5]:", list2[1:5])

print("\n")




#program 2

list=['physics','chemistry',1997,2000]
print("values available at index 2:")
print(list[2])

print("new value available at index 2")
print(list[2])

print("\n")


#program 3

def defArgfunc(empname,emprole="Manager"):
    print("emp name :", empname)
    print("emp role:",emprole)

    return

print("using default value")
defArgfunc(empname="Nick")

print("*****************************")

print("overwriting default value")
defArgfunc(empname="ram",emprole="CEO")

print("\n")


#program 4

tuple=('abcd',786,2.34,'Thon',70.2)
tinytuple=(123,'jhon')
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2: ])
print(tinytuple * 2)
#print(tuple*tinytuple)
