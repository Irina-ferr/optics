import numpy as np
import matplotlib.pyplot as plt

# Исходные данные
data = [
    (0, 1.333), 
    (25, 1.339),
    (50, 1.349),
]

x = np.array([point[0] for point in data])
y = np.array([point[1] for point in data])

# Аппроксимация полиномом второй степени
coefficients = np.polyfit(x, y, 2)
poly = np.poly1d(coefficients)

# Функция для нахождения x по заданному y
def find_x(y_val, coefficients):
    a, b, c = coefficients[0], coefficients[1], coefficients[2] - y_val
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return None
    sqrt_disc = np.sqrt(discriminant)
    x1 = (-b + sqrt_disc) / (2 * a)
    x2 = (-b - sqrt_disc) / (2 * a)
    # Выбор корня в диапазоне исходных данных
    valid_x = [xi for xi in [x1, x2] if x.min() <= xi <= x.max()]
    return valid_x[0] if valid_x else None

# Поиск x для заданных y
y_values_to_find = [1.339]
results = {}
for y_val in y_values_to_find:
    x_val = find_x(y_val, coefficients)
    results[y_val] = x_val

# Построение графика
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', label='Исходные данные')
x_fit = np.linspace(x.min(), x.max(), 100)
y_fit = poly(x_fit)
plt.plot(x_fit, y_fit, color='orange', label='Аппроксимирующая кривая')

# Отображение найденных точек
for y_val, x_val in results.items():
    plt.scatter(x_val, y_val, color='red', zorder=5, label=f'Найдено: y={y_val} → x={x_val:.2f}')

plt.xlabel('Содержание спирта, %')
plt.ylabel('Коэффициент преломления')
plt.legend()
plt.grid(True)

# Вывод результатов
print("Найденные значения x для заданных y:")
for y_val, x_val in results.items():
    print(f"y = {y_val} → x = {x_val:.2f}")

plt.show()