#Tuples

a = [1,2,3]
a[0] = 100
a[2] = 200
print(a)

a = (1,2,3,4)
print(type(a))
#a[0]=1--->immutable

def func(*args):
    print(type(args))
func(1,2,3,4)

a = 5
b = 9
a,b = b,a
c = a,b
print(type(c))

def sum_diff(a,b):
    s = a + b
    d = a - b
    return s,d
c = sum_diff(10,5)
print(type(c))

s,d = sum_diff(10,5)
print(s,d) #unpack iterables

a = 1,2,3,4
print(type(a))

print(list(a))
print(tuple(a))

print(list(range(0,5)))

#Dictionaries

a = dict()
a = {
    "name":"Jatin Katyal",
    1: "something",
    (1,2): "Tuple key wat?"
    }
  #Can't index with list--->Unhashable type  
print(a["name"])


a = {
    "name":"jatin",
    "company":"shuttl",
    "college":"LPU"
}
#print(a["marks"])--->Key Error

key = "marks"
if key in a:
    print(a[key])
else:
    print("Key doesn't exists")


#Some Dict Methods
#get()
a = {
    "name":"jatin",
    "company":"shuttl",
    "college":"LPU"
}
print(a.get(key)) #safe method, doesn't return error instead give None
print(a.get(key,"Key doesn't exists"))

#keys()
print(a.keys())

#values()
print(a.values())

#items()
for i in a.items():
    print(i)       

for key,value in a.items(): #Unpacking
    print(key,"--->",value) 

for i in a:
    print(i)

print(list(a))

#clear()
a.clear()
print(a)

#NOTE: Keys of dictionary can be any immutable object, since keys can't be changed 


Write a simple python program which inputs and stores the data about university students as a list of dictionaries.
Your final record structure should look like this.
{
    {
        'roll-no':1211,
        'name':Ravi,
        'branch':CSE,
    },
    {
        'roll-no':202,
        'name':Abhishek,
        'branch':SE,
    },
    {
        'roll-no':1202,
        'name':Sachin,
        'branch':IT,
    }
}

n = int(input("Enter n: ")) 
dic = {} 
for i in range(n):
    d={}
    record_no = int(input("Enter record no: ")) 
    roll_no = int(input("Enter roll no: ")) 
    name = input("Enter name: ") 
    branch = input("Enter branch: ") 
    d["roll-no"] = roll_no
    d["name"] = name
    d["branch"] = branch
    dic[record_no] = d
