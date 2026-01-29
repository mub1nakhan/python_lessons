# Integer misollari
age = 25
temperature = -10
year = 2026

print(type(age))  # <class 'int'>

# Matematik amallar
a = 10
b = 3
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3 (butun qism)
print(a % b)   # 1 (qoldiq)
print(a ** b)  # 1000 (daraja)

# Float misollar
weight = 43.4
height = 1.77

print(type(weight)) #<class "float">
a = 21.2
b = 12.3
print(a + b)

#floatni integerga almashtirish
numb = 12.3
print(int(numb))

# String yaratish
name = "Ali"
surname = 'Valiyev'
message = "Hello, World!"

print(type(name))  # <class 'str'>

# String metodlari
text = "python dasturlash"

print(text.upper())      # PYTHON DASTURLASH
print(text.lower())      # python dasturlash
print(text.capitalize()) # Python dasturlash
print(text.title())      # Python Dasturlash

# String qo'shish 
first_name = "Ali"
last_name = "Valiyev"
full_name = first_name + " " + last_name
print(full_name)  # Ali Valiyev

# f-string (formatted string)
age = 20
print(f"Mening ismim {first_name}, yoshim {age}")

# String uzunligi
text = "Hello"
print(len(text))  # 5

# Indexing va Slicing
word = "Python"
print(word[0])     # P (birinchi harf)
print(word[-1])    # n (oxirgi harf)
print(word[0:3])   # Pyt
print(word[2:])    # thon
print(word[:4])    # Pyth

# Boolean misollari
is_student = True
is_worker = False

print(type(is_student))  # <class 'bool'>

# Taqqoslash operatorlari
x = 10
y = 20

print(x > y)   # False
print(x < y)   # True
print(x == y)  # False
print(x != y)  # True

# Mantiqiy operatorlar
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False