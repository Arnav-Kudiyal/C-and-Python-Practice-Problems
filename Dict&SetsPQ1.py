# Question 1
words = {
    "table" : ["a piece of furniture", " list of facts and figures"],
    "cat" : "a small animal"
}

print(words)

#Question 2

subjects = {"python", "java", "C++","python", "javascript","java","python","java","C++","C"}

total_classrooms = len(subjects)

print(f"The total number of classrooms needed are {total_classrooms}")


#Question 3

maths = int(input("Enter the marks of the maths"))
phy = int(input("Enter the marks of the Physics"))
hindi = int(input("Enter the marks of the Hindi"))

marks = {}

marks.update({"Maths": maths})
marks.update({"Physics" : phy})
marks.update({"Hindi" : hindi})

print(marks)

#Question 4

number = {9,"9.0"}
print(number)