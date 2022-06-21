import numpy as np

absolute_null = -273

while True:
    live_boar_temp = int(input("Введите темепературу живого кабана: "))
    arrest_boar_temp = int(input('Введите температуру найденного кабана: '))
    later_boar_temp = int(input("Введите температуру кабана спустя час после задержания: "))
    air_temp = int(input("Введите температуру воздуха: "))
    waiting_time = int(input("Введите время ожидания браконьеров: "))

    if live_boar_temp < absolute_null or arrest_boar_temp < absolute_null or later_boar_temp < absolute_null \
            or air_temp < absolute_null:
        print("Температура не может быть ниже абсолютного ноля")
        continue

    if live_boar_temp >= arrest_boar_temp >= later_boar_temp >= air_temp:
        break

    print("Некорректное изменение температуры")

proportionality_ratio = np.log((arrest_boar_temp - air_temp) / (later_boar_temp - air_temp))
estimated_death_time = (1 / proportionality_ratio) * np.log((live_boar_temp - air_temp) / (arrest_boar_temp - air_temp))
print("Убийство произошло за ", estimated_death_time, " часа до задержания.")

if estimated_death_time > waiting_time:
    print("Ну наверное браконьеры виновны?? Нет доказательств")
else:
    print("Убийство произошло у нас на глазах а мы просто смотрели, но зато мы точно видели настоящих браконьеров")

