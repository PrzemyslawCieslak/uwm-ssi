plik = open("C01/diabetes.txt", "r")
plik2 = open("C01/diabetes-type.txt", "r")

slownik = {}
slownik2 = {}

for x in plik2:
    line = x
    line = line.strip()
    line = line.split(" ")
    slownik2[line[0]] = line[1]

indexesOfNumbers = []
i = 1
for key in slownik2:
    if slownik2[key] == "n":
        indexesOfNumbers.append(i)
    i += 1

for x in plik:
    line = x
    line = line.strip()
    line = line.split(" ")

    if line[-1] in slownik:
        slownik[line[-1]] = slownik.get(line[-1]) + [line]
    else:
        slownik[line[-1]] = [line]


print("Istniejące klasy decycyzyjne + liczba elementów w klasie: ")
for key in slownik:
    print("{}, liczba elementów: {}".format(key, len(slownik[key])))

