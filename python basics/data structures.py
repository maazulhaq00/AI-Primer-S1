#-------------> list : ordered, mutables, indexed, duplicate values can be stored

# fruits = ["apple", "mango", "banana", "apple"]

# print(fruits)

# for f in fruits:
#     print("The fruit is " + f)

# fruits[1] = "orange"
# print(fruits)

# fruits.append("mango")
# print(fruits)

# fruits.insert(2, "gauva")
# print(fruits)

# fruits.pop()
# print(fruits)

# fruits.remove("orange")
# print(fruits)

#-------------> tuple : ordered, immutable, indexed, duplicate values can be stored

# grade = ("A+", "A", "B", "C", "Fail")

# print(grade[1])
# print(len(grade))

# grade[4] = "F" # error
# print(grade)

# grade.append("D") # error
# print(grade)

# tuple unpacking

# student = ("Ali", 24, "Karachi")

# name, age, city = student

# print(f"name: {name}, age: {age}, city: {city}")

# print("A+" in grade)

# print("D" in grade)

#------------->  sets : unordered, unindexed, unique items

# courses = {"JS", "Bootstrap", "Markup Language", "JS"}
# print(courses)

# courses.add("C#")
# print(courses)

# courses.remove("Markup Language")
# print(courses)

# # courses.remove("Python") # error
# # print(courses)

# courses.discard("Python") 
# print(courses)

# for course in courses:
#     print(course)


# print("JS" in courses)


# courses2 = {"HTML", "Bootstrap", "Python"}

# print(courses | courses2) # union
# print(courses & courses2) # intersection
# print(courses - courses2) # difference
# print(courses2 - courses) # difference
# print(courses2 ^ courses) # symmetric difference



#-------------> dictionary : key-values pair
product = {
    "title": "Eco friendly water bottle",
    "price": 1700,
    "rating": 4.8
}

print(product)
print(product["title"])
#print(product["stock"]) # error
print(product.get("title"))
print(product.get("stock"))

product["price"] = 1800
product["stock"] = 25
print(product)

print(len(product))

print("stock" in product)

for key in product:
    print(f"{key} is {product[key]}")

del product["stock"]
print(product)
