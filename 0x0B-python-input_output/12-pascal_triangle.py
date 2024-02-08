#!/usr/bin/python3
"""A Pascal's Triangle function."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the triangle."""

    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri_angle = triangles[-1]
        tmp = [1]
        for i in range(len(tri_angle) - 1):
            tmp.append(tri_angle[i] + tri_angle[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
