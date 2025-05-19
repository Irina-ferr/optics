import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Исходные данные
data = [
    (0, 1.333), 
    (25, 1.339),
    (50, 1.349),
]

x = np.array([point[0] for point in data])
y = np.array([point[1] for point in data])

# Определение линейной функции для аппроксимации
def linear_func(x, a, b):
    return a * x + b

# Выполнение аппроксимации
params, covariance = curve_fit(linear_func, x, y)
a, b = params

# Поиск x для заданных y
y_values_to_find = [1.339]
results = {}
for y_val in y_values_to_find:
    x_val = (y_val - b) / a
    results[y_val] = x_val

# Построение графика
plt.scatter(x, y, label='Исходные данные', zorder=5)
x_fit = np.linspace(min(x), max(x), 100)
y_fit = linear_func(x_fit, a, b)
plt.plot(x_fit, y_fit, 'r-', label='Аппроксимирующая прямая')

# Отметка найденной точки
for y_val, x_val in results.items():
    plt.scatter(x_val, y_val, color='green', zorder=5, 
                label=f'Найденная точка: x={x_val:.2f}%')

plt.xlabel('Содержание спирта, %')
plt.ylabel('Коэффициент преломления')
plt.legend()
plt.grid(True)

# Вывод результатов
print("Найденные значения x для заданных y:")
for y_val, x_val in results.items():
    print(f"y = {y_val} → x = {x_val:.2f}%")

plt.show()