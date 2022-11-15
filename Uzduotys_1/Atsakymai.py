# Uzduotis 1 #

a = int(input("Įveskite skaičių a "))
b = int(input("Įveskite skaičių b "))
if b > a:
    print("a mažesnis už b")
elif a == b:
    print("a lygu b")
else:
    print("a didesnis už b")

# Uzduotis 2 #

zodis = "Zen of Python"
print(zodis[5])
print(zodis[-6])
print(zodis[:3])
print(zodis[-6:])
print(zodis[::-1])
print(zodis.split())
print(zodis.replace("Python", "Programming"))


# Uzduotis 3 #

zodis = "The Zen of Python"

print(zodis.upper())
print(zodis.casefold())
print(zodis.capitalize())
print(zodis.count("e"))
print(zodis.count("Zen"))

# Uzduotis 4 #

a = int(input("Įveskite pirmą skaičių "))
b = int(input("Įveskite antrą skaičių "))
c = input("Pasirinkite matematinį veiksmą (+, -, *, /): ")

if c == "+":
    print("Skaičių suma lygi: ", a + b)
if c == "-":
    print("Skaičių atimtis lygi: ", a - b)
if c == "*":
    print("Skaičių daugyba lygi: ", a * b)
if c == "/":
    print("Skaičių dalyba lygi: ", a / b)


# Uzduotis 4 #

skaicius = int(input("Įveskite skaičių: "))

if skaicius % 2 == 0:
    print("Įvestas skaičius yra lyginis!")
else:
    print("Įvestas skaičius yra nelyginis!")

if skaicius % 3 == 0:
    print("Įvestas skaičius dalinasi iš trijų")   