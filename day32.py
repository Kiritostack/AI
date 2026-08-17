matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

result = []

for row in matrix:
    new_row = []

    for value in row:
        if value % 2 == 0:
            new_row.append(value * 10)

    result.append(new_row)

print(result)