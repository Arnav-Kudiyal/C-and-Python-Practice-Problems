# WAP to input user's first name & print its lenght

name = str(input("Enter your first name"))
print(len(name))

#WAP to find the occurance of "$" in a string

word = str(input("Enter you String"))
print(word.count("$"))

#WAP grade student based on marks

english = int(input("Enter your marks in English"))
maths = int(input("Enter your marks in Maths"))
cs = int(input("Enter your marks in Computer Science"))
physics = int(input("Enter your marks in Physics"))
chemistry = int(input("Enter your marks in Chemistry"))

total = english+maths+cs+physics+chemistry

per = (total/500)*100

if(per>=90):
    print("A")
elif(per>=80):
    print("B")
elif(per>=70):
    print("C")
else:
    print("D")

#WAP to check if the number is even or odd
number = int(input("Enter the number"))

if(number %2 == 0):
    print("The number is even")
else:
    print("The number is odd")

#WAP to find the greatest of 3 numbers entered by the user

a = int(input("Enter First Number"))
b = int(input("Enter Second Number"))
c = int(input("Enter Third Number"))

if(a>b and a>c):
    print("A is greater")
elif(b>a and b>c):
    print("B is greater")
else:
    print("C is greater")

#WAP to check if the number is a multiple of 7 or not

a = int(input("Enter the number"))

if(a %7==0):
    print("It is a multiple of 7")
else:
    print("Its not a multiple of 7")