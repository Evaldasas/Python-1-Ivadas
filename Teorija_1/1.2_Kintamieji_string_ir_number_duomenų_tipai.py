########################################################################################################Kintamieji (skaičiai):


#############################           Sveikieji skaičiai – Integer (int):

a = 5
print(a)

# 5

a = int(5)
print(a)

# 5

a = 7
print(a)

# 7

a = 10
print(a)

# 10

a = a - 4
print(a)

# 6


##############################################      Skaičiai su kableliu – float:

a = 8.56
b = 5
c = a + b
print(c)

# 13.56
a = float(5)
print(a)

# 5.00


####################################################     Veiksmai su kintamaisiais:

a = 5 + 2
print(a)
 
# 7

b = 5 - 2
print(b)
 
# 3

c = 5 * 2
print(c)
 
# 10

d = 5 / 2
print(d)
 
# 2.5


############################################################################################        Kintamųjų pavadinimų sudarymo taisyklės
# Kintamųjų pavadinimai turi prasidėti raide arba pabraukimu, pvz:

_vardas

vardas

# Likusioji kintamojo dalis gali būti sudaryta iš raidžių, skaičių ir pabraukimų:

pirmas1

antras_skaicius

_e5786

# Pavadinimuose svarbios didžiosios ir mažosios raidės:

# Vardas ir vardas būtų skirtingi kintamieji.


# Kintamaisiais negali būti python raktiniai žodžiai:

'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'



# Python kalboje sudurtinius kintamųjų pavadinimus priimta sudarinėti taip:

first_block, vandens_temperatura



##############################################      Paprastesnis veiksmų atlikimas:

a = 5
a += 2
print(a)

# 7

b = 12
b /= 3
print(b)

# 4.0


##################################          Kėlimas laipsniu:

a = 2**2
print(a)

# 4

b = 5**3
print(b)

# 125



###########################################     Sveikojo skaičiaus ir liekanos paieška (div/mod):

a = 32 / 6
print(a)

# 5.333333333333333

b = 32 // 6
print(b)

# 5

c = 32 % 6
print(c)

# 2


##############################################      Simbolių eilutės (String) tipas:

zodis1 = "Labas "
print(zodis1)

# Labas

zodis2 = str("vakaras")
print(zodis2)

# vakaras

print(zodis1 + zodis2)

# Labas vakaras


##################################################          Nauja eilutė:

print("Labas \nvakaras")

# Labas
# vakaras


##################################################          Veiksmai su simbolių eilėmis (String):


zodis = "Code Academy"

print(zodis[5])

# A

print(zodis[-2])

# m

print(zodis[5:12])

# Academy

print(zodis[5:])

# Academy

print(zodis[:4])

# Code

print(zodis[5:12:1])

# Academy

print(zodis[5::2])

# Aaey

print(zodis[::-1])

# ymedacA edoC

print(zodis.split())

# ['Code', 'Academy']

print(zodis.upper())

# CODE ACADEMY

print(zodis.replace('c', 'k'))

# Code Akademy

print(zodis.replace('Code', 'Music'))

# Music Academy


######################################################              Geras būdas formuoti stringus iš kintamųjų:

a = 5

zodis = "Labas"
dar_vienas = "Šitas žodis"

print("a lygu: " + str(a) + ", žodis: " + zodis + ", dar vienas žodis – " + dar_vienas)

# Geresnis variantas:
print(f"a lygu {a}, žodis: {zodis}, dar vienas žodis – {dar_vienas}")


########################################            Veiksmai su skirtingais tipais (konvertavimas):

d = "Žodis "
e = 5
print(d+e)

# TypeError: can only concatenate str (not "int") to str

e = str(e)
print(d+e)

# Žodis 5

a = "250"
b = 4
print(a * b)

# ???


##########################################################################            Kintamųjų įvedimas ir išvedimas:


##############################################String įvedimas:


a = input("Įveskite pirmą žodį ")
b = input("Įveskite antrą žodį ")
print("Jūsų sakinys: ", a + b)

# Įveskite pirmą žodį Python
# Įveskite antrą žodį programavimas
# Jūsų sakinys: Python programavimas


########################            Integer, Float įvedimas:


a = int(input("Įveskite pirmą skaičių "))
b = int(input("Įveskite antrą skaičių "))
print("Jūsų skaičių suma: ", a + b)

# Įveskite pirmą skaičių 5
# Įveskite antrą skaičių 6
# Jūsų skaičių suma: 11

h = float(input("Įveskite skaičių "))
print(h)
 