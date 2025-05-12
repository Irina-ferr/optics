import numpy as np
import matplotlib.pyplot as plt

# Исходные данные
data = [
    (623.4, 2731), 
    (612.3, 2500.3),
    (579.1, 2301),
    (577, 2297),
    (546.1, 2107),
    (491.6, 1688),
    (435.8, 1027),
    (434.7, 1006),
    (433.9, 993),
    (410.8, 591),
    (407.7, 531.6),
    (404.7, 469),
]

x = np.array([point[0] for point in data])
y = np.array([point[1] for point in data])

# Значения y, для которых нужно найти x
y_values_to_find = [754, 866.3, 973, 1470.6, 2022.6, 2064, 2322, 2558, 2826]

# Аппроксимация полиномом 3-й степени
degree = 3
coefficients = np.polyfit(x, y, degree)
poly = np.poly1d(coefficients)

# Функция для поиска x по заданному y
def find_x(y_val, poly_coeffs, x_min, x_max):
    adjusted_coeffs = list(poly_coeffs)
    adjusted_coeffs[-1] -= y_val
    roots = np.roots(adjusted_coeffs)
    real_roots = roots[np.isreal(roots)].real
    valid_roots = [r for r in real_roots if x_min <= r <= x_max]
    return valid_roots[0] if valid_roots else None

# Поиск x для каждого y из списка
x_min, x_max = min(x), max(x)
results = {}
for y_val in y_values_to_find:
    x_val = find_x(y_val, coefficients, x_min, x_max)
    results[y_val] = x_val

# Визуализация
plt.scatter(x, y, label='Исходные данные', color='blue')
x_fit = np.linspace(x_min, x_max, 500)
plt.plot(x_fit, poly(x_fit), label='Аппроксимация', color='red')

# Отметить найденные точки
for y_val, x_val in results.items():
    if (y_val==754):
        plt.scatter(x_val, y_val,label='Найденные точки', color='green', zorder=5)
    else:
        plt.scatter(x_val, y_val, color='green', zorder=5)

        # plt.text(x_val, y_val, f'({x_val:.1f}, {y_val})', fontsize=8)

plt.xlabel('φ, °')
plt.ylabel('Длина волны')
plt.legend()
plt.grid(True)
# Вывод результатов
print("Найденные значения x для заданных y:")
for y_val, x_val in results.items():
    print(f"y = {y_val}→ x = {x_val}")
plt.show()

