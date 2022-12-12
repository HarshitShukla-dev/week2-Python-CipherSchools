print(1,2,3,4,5,sep=",")

#Positional Arguments
#Mapping w.r.t position
def func(a,b,c):
    print(a)
    print(b)
    print(c)
func(1,2,3)

#keyworded arguments
def func(a,b,c):
    print(a)
    print(b)
    print(c)
func(a = 1,b = 2,c = 3)

def func(a):
    print(a)
#func() ---> Raise error
func(1)

def hello():
    print("Hello World !")
hello #<function__main__.hello()>
hello()
#hello=<function defination>
a = 1
a = hello
a()

print(type(a))
hello = 2
print(hello) #hello is no mroe a function
a() #a is still a fumnction

def b():
    print("Hi")
def b():
    print("Bye")

#required arguments
def func(a,b):
    print(a,b)
func(1,2)

#default arguments
def func(a = 1,b = 2):
    print(a,b)
func()
func(1)
func(1,2)

#optional arguments
def func(*a):
    print(*a)
func(1,2,3,4)

#required keyworded only arguments
def func(a,b,*c):
    print(a)
    print(b)
    print(c)
func(1,2,3,4,"smriti",1.5)

#default keyworded only arguments
def func(a,b,*c,d,e="smriti"):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
func(1,2,3,4,5,6,7,d=8)

#optional keyworded only arguments
def func(**k):
    print(k)
func(a = 1,b = 2)

print(sorted([1,4,3,8,6]))
#Anonymous functions or lambda functions
#lambda is always a one liner function, it can only contain a single expression inside it
a = lambda a,b: a+b #Expression that return a function
print(a(1,2))

a = 1
b = 2
c = print(a,b)
print(c) #return None
