n = int(input("Введите количество строк (n): "))
m = int(input("Введите количество столбцов (m): "))

print("\nПРЯМОУГОЛЬНИК", n, "x", m)
for i in range(n):
    print("#" * m)

print("\nПРАВЫЙ ТРЕУГОЛЬНИК:")
for i in range(1, n + 1):
    print("#" * i)

print("\nРАМКА", n, "*", m)
for i in range(n):
    if i == 0 or i == n - 1:
        print("#" * m)
    else:
        print("#" + " " * (m - 2) + "#")
