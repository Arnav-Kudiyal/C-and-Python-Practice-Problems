a = "this  isa double quote's string"      #Double qoute string
b = 'This is a single quote string'        #Single Quote String
c = """ This is a multi line string"""    #Multi line string

d = len(a)  #Length of string
print(d)

print(a[3]) #Indexig

print(a[3:10]) #Slicing

print(a[-10 :-1]) #Negative Index Slicing

print(a.endswith("ring"))  #If strings ends with given word

print(a.capitalize()) #Capitalize Ist character of string

print(a.replace("o", "a")) #Replace old value to new value

print(a.find("double")) #Finds the value and gives the index of first occurance

print(a.count("is")) # Counts the occurnce of a value in a string

#CONDITIONAL STATEMENTS

age = 16
if(age >18):
    print("You are eligible to vote")
elif(age == 18):
    print("You are eligible to vote")
else:
    print("Your are not eligible to vote")


