################################################                Sąlyga IF (jeigu):

#########################           Jeigu (IF) [sąlyga], tuomet [veiksmas]


if 5 > 0:
    print("5 yra daugiau už 0")
# 5 yra daugiau už 0

if 5 < 0:
    print("5 yra daugiau už 0")
print("Programa baigta")

# Programa baigta


skaicius = 25
if skaicius < 100:
    print("1: Skaičius yra mažesnis už 100")
if skaicius > 10:
    print("2: Skaičius yra didesnis už 10")
if skaicius < 10:
    print("3: Skaičius yra mažesnis už 10")

# 1: Skaičius yra mažesnis už 100
# 2: Skaičius yra didesnis už 10

skaicius = 60
if skaicius < 70:
    print("Skaičius yra mažesnis už 70")
    if skaicius > 15:
        print("Skaičius yra tarp 15 ir 70")

# Skaičius yra mažesnis už 70
# Skaičius yra tarp 15 ir 70

skaicius = 10

# Skaičius yra mažesnis už 70


#######################################################         Sąlyga ELSE (jei ne, tuomet):

skaicius = 56
if skaicius == 50:
    print("1: Skaičius yra lygus 50")
else:
    print("2: Skaičius nelygus 50")

# 2: Skaičius nelygus 50


######################################################          Sąlyga ELIF (jei sąlyga netenkinama ir jei):

skaicius = 0

if skaicius > 0:
    print("Teigiamas skaičius")
elif skaicius == 0:
    print("Nulis")
else:
    print("Neigiamas skaičius")

# Nulis