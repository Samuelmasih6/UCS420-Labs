print("hello world")
a=2
b=3
print(a+b)
name="rajat "
verb="is "
relation="friend"
print(name+verb+relation)
age=20
end="years old"
print(name,age,end)

print(3*"Samuel")
for i in range(3):
    print("Samuel")

#assignment 2.1
def add(a,b,c):
    return a+b+c

a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
result=add(a,b,c)
print("addition:", result)

print("printing 10 numbers")
for i in range(10):
    print(i)

print("printing 1-10 with by 2 gaps")
for i in range(1,10,2):
    print(i)

print("while Loop")
i=1
while i<=10:
    print(i)
    i=i+1

for i in range(1,11):
    print("5 *",i,"=",5*i)

print(*range(1,10))
