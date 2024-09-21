import math

# Function to calculate the area of a triangle using Heron's formula
def calculate_area(a, b, c):
    p = (a + b + c) / 2.0
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

# Function to sort triangles based on their area
def sort_triangles(triangles):
    # Bubble sort based on the area of each triangle
    n = len(triangles)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if calculate_area(*triangles[j]) > calculate_area(*triangles[j + 1]):
                # Swap triangles if the area of the current triangle is greater
                triangles[j], triangles[j + 1] = triangles[j + 1], triangles[j]

# Main program
n = int(input())  # Number of triangles
triangles = []

# Reading the triangle sides
for i in range(n):
    a, b, c = map(int, input().split())
    triangles.append([a, b, c])

# Sorting the triangles based on their area
sort_triangles(triangles)

# Printing the sorted triangles
for triangle in triangles:
    print(triangle[0], triangle[1], triangle[2])
