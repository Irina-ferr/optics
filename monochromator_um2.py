import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# данные в формате (x,y)
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

# преобразуем данные в numpy массивы
x_data = np.array([point[0] for point in data])
y_data = np.array([point[1] for point in data])

# создаем интерполяционную функцию
interp_func = interp1d(x_data, y_data, kind='cubic', fill_value="extrapolate")

# задаем значения y для которых нужно найти x
y_values_to_find = [754, 866.3, 973, 1470.6, 2022.6, 2064, 2322, 2558, 2826]

# находим соответствующие x для указанных y
x_found = []

# генерируем x-значения для интерполяции
x_candidates = np.linspace(min(x_data), max(x_data), 1000)
y_candidates = interp_func(x_candidates)

# для каждого y находим соответствующее x
for y in y_values_to_find:
    # находим ближайший x для каждого y
    closest_x = x_candidates[np.abs(y_candidates - y).argmin()]
    x_found.append(closest_x)

# выводим найденные значения x
for y, x in zip(y_values_to_find, x_found):
    print(f"Для y = {y} найдено x ≈ {x:.2f}")

# построение графиков
plt.figure(figsize=(12, 10))

# график исходных данных
plt.subplot(2, 1, 1)
plt.scatter(y_data, x_data, color='red', label='Исходные точки')
plt.plot(interp_func(x_candidates), x_candidates, 'g--', label='Интерполяция')
plt.title('Исходные данные')
plt.xlabel('< ϕ 3>, °')
plt.ylabel('Длина волны')
plt.grid()
plt.legend()

# график с интерполяцией и определяемыми точками
plt.subplot(2, 1, 2)
plt.scatter(y_data, x_data, color='red', label='Исходные точки')
plt.scatter(y_values_to_find, x_found, color='black', label='Определяемые точки')
plt.plot(interp_func(x_candidates), x_candidates, 'g--', label='Интерполяция')

# добавление вертикальных линий для каждого y
for y in y_values_to_find:
    plt.axvline(x=y, color='orange', linestyle='--', linewidth=0.8)

plt.title('График с интерполяцией и определяемыми точками')
plt.xlabel('< ϕ 3>, °')
plt.ylabel('Длина волны')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
