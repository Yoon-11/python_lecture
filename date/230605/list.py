matrix = []
numberOfRows = eval(input("Enter the number of rows : "))
numberOfColumns = eval(input("Enter the number of columns : "))

for row in range(0, numberOfRows):
    matrix.append([])
    for colum in range(0, numberOfColumns):
        value = eval(input("Enter an element and press Enter : "))
        matrix[row].append(value)

print(matrix)