import math

def distance(x1, y1, x2, y2):
    length = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return length

def angle(side1, side2, side3, name):
    sides = [side1, side2, side3]
    sides.sort()
    output = open(name, "w")
    if sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2:
        print("Треугольник прямоугольный")
        print("Треугольник прямоугольный", file = output)
        for i in sides:
            print("Длина стороны ", sides.index(i)+1, " = ", i)
            print("Длина стороны ", sides.index(i)+1, " = ", i, file = output)
        print("Площадь = ", sides[0]*sides[1]/2)
        print("Биссектриса прямого угла = ", math.sqrt(2)*sides[0]*sides[1] / (sides[0]+sides[1]))
        print("Биссектриса катета 1 = ", sides[0]*math.sqrt(2*sides[2]/(sides[0]+sides[2])))
        print("Биссектриса катета 2 = ", sides[1]*math.sqrt(2*sides[2]/(sides[1]+sides[2])))
        print("Площадь = ", sides[0] * sides[1] / 2, file = output)
        print("Биссектриса прямого угла = ", math.sqrt(2) * sides[0] * sides[1] / (sides[0] + sides[1]), file = output)
        print("Биссектриса катета 1 = ", sides[0] * math.sqrt(2 * sides[2] / (sides[0] + sides[2])), file = output)
        print("Биссектриса катета 2 = ", sides[1] * math.sqrt(2 * sides[2] / (sides[1] + sides[2])), file = output)
    elif sides[2] ** 2 < sides[0] ** 2 + sides[1] ** 2:
        print("Треугольник остроугольный")
    else:
        print("Треугольник тупоугольный")

    output.close()

def type(side1, side2, side3, name):

    output = open(name, "a")
    if side1 == side2 == side3:
        print("Треугольник равносторонний")
        print("Треугольник равносторонний", file = output)
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("Треугольник равнобедренный")
        print("Треугольник равнобедренный", file = output)
    else:
        print("Треугольник разносторонний")
        print("Треугольник разносторонний", file = output)



# Main

x, y = [], []

name1 = input("Введите имя файла с координатами ")
name2 = input("Введите имя файла с результатами ")
coordinates = open(name1)
countSpace = 0
countDigit = 0
countMinus = 0
for line in coordinates:
    if any(c.isspace for c in line):
        countSpace += 1
    if not any(c.isalpha for c in line) and countSpace == 3: 
        print("Ошибка. В файле находятся не подходящие данные.")
        exit(1)
    else:
        pass
coordinates.close()

coordinates = open(name1)
for line in coordinates:
    row = line.split()
    x.append(float(row[0]))
    y.append(float(row[1]))
coordinates.close()

for i in x:
    side1 = distance(x[0], y[0], x[1], y[1])
    side2 = distance(x[0], y[0], x[2], y[2])
    side3 = distance(x[1], y[1], x[2], y[2])

angle(side1, side2, side3, name2)
type(side1, side2, side3, name2)
