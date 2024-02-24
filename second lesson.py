def generate_pascal_triangle(rows):
    triangle = []
    
    for i in range(rows):
        row = [1] * (i + 1)
        for j in range(1, len(row) - 1):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
        
    return triangle

def print_pascal_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)))

rows = 5
pascal_triangle = generate_pascal_triangle(rows)
print_pascal_triangle(pascal_triangle)
