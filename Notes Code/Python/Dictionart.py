info = {
    "name" : "Arnav",
    "Class" : "BCA",
    "Roll_No" : 86,
    "subjects" : ["DSA","C++","Digital"],
    "score" : (23,54,58,45)
}

print(info)  
print(type(info))

print(info["Roll_No"])
info["Roll_No"] = 87
print(info["Roll_No"])

# Nested Dictionary

student = {
    "name" : "Arnav",
    "subject" : {
        "Maths" : 30,
        "Science" : 60
    }
}

print(student["subject"]["Maths"])

# Dictionary Meathods

print(student.keys())

print(len(student.keys()))

# value function

print(student.values())\

# .items meathod

print(list(student.items()))

# .get meathod

print(student.get("name"))

# .update meathods
student.update({"city" : "Delhi"})

