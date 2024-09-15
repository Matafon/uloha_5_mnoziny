n = int(input("Zadej velikost množiny:"))

print("Uspořádané trojice: ")

x = 0
seznam = []

while x < n:
    y = 0
    x += 1
    while y < n:
        z = 0
        y += 1
        while z < n:
            z += 1
            print(str(x) + str(y) + str(z), end=", ")
            if x != y and x!= z and y != z and x < y < z:
                hodnota = str(x) + str(y) + str(z)
                seznam.append(hodnota)

print("\n" + "3prvkové podmnožiny:" + str(seznam))