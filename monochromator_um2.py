import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

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

# Преобразуем данные в массивы NumPy
x_data = np.array([point[0] for point in data])
y_data = np.array([point[1] for point in data])

# Заданные значения y для поиска x
y_values_to_find = [754, 866.3, 973, 1470.6, 2022.6, 2064, 2322, 2558, 2826]

# Определение линейной функции для аппроксимации
def linear_func(x, k, b):
    return k * x + b

# Аппроксимация данных
params, _ = curve_fit(linear_func, x_data, y_data)
k_fit, b_fit = params

# Вычисление x для заданных y
y_values = np.array(y_values_to_find)
x_values = (y_values - b_fit) / k_fit

# Вывод результатов
print("Аппроксимирующая прямая: y = {:.2f}x + {:.2f}".format(k_fit, b_fit))
print("\nНайденные значения x для заданных y:")
for y, x in zip(y_values_to_find, x_values):
    print(f"y = {y}\t→ x = {x:.2f}")

# Построение графика
plt.scatter(x_data, y_data, label='Исходные данные')
plt.plot(x_data, linear_func(x_data, k_fit, b_fit), 'r-', label='Аппроксимирующая прямая')
plt.scatter(x_values, y_values, color='green', zorder=5, label='Найденные точки')
plt.title('График с интерполяцией и определяемыми точками')
plt.xlabel('< ϕ >, °')
plt.ylabel('Длина волны')
plt.legend()
plt.grid(True)
plt.show()