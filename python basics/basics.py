name="Ali"
age=18
print("My name is " + name + ". I am " + str(age) + " year old.")

# cond
if age < 18:
    print("=============================")
    print("You are not eligible to VOTE.")
    print("=============================")
elif age == 18:
    print("=============================")
    print("Welcome NEW VOTER !!!.")
    print("=============================") 
else:
    print("=============================")
    print("You are eligible to VOTE.")
    print("=============================") 

# func
def calculateDiscount(total, percent):
    discount_amount = total*percent/100
    print("Discount is " + str(discount_amount))

calculateDiscount(total=980, percent=10)
calculateDiscount(total=3643, percent=54)

# complex data type
# root = 3+5j
# print(type(root))

# input & interpulation
def addition():
    print("Enter number 1:")
    num1 = input()
    print("Enter number 2:")
    num2 = input()

    sum = float(num1) + float(num2)

    print(f"The addition of {num1} and {num2} is {sum}")

# addition()

# Loops
def genrateTable():
    num1 = input("Enter a number: ")
    num = int(num1)
    i = 1
    while i <= 10:
        print(f"{num} x {i} = {num*i}")
        i = i + 1

genrateTable()

students = ["Ayesha", "Abrish", "Ahmed", "Ali"]

for std in students:
    print(f"name is {std}")

for i in range(3, 8 ,2): #3, 5, 7
    print(i)

for i in "Maaz": #M, a, a, z
    print(i)



