#!/usr/bin/python3
"""
Create a function def pascal_triangle(n): that returns a list of lists of
integers representing the Pascal’s triangle of n:

 Returns an empty list if n <= 0
 You can assume n will be always an integer
 """
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        if i == 0:
            row = [1]
        else:
            prev_row = triangle[-1]
            row = [1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)
        triangle.append(row)

    return triangle
