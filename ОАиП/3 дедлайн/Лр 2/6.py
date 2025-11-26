def flat_gen(nested_list):
    for sublist in nested_list:
        for item in sublist:
            yield item

matrix = [
    [9, 8, 7],
    [6, 5],
    [4, 3, 2, 1]
]

for num in flat_gen(matrix):
    print(num, end="")
