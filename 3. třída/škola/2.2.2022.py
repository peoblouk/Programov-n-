"""
course = " python programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.rstrip())
print(course.find("Pro"))
print(course.replace("p", "j"))

print(course.count("python"))

course.replace("python", "Universe")
print(course)


# postupně se vypisuje
greeting = "Hello"
name = "Petr"

message = "{}, {}. Welcome!".format(greeting, name)
print(message)

"""
name = "Petr"
print("Hello %d")