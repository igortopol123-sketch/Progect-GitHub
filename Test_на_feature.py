# import result
import requests
# import response
# import pytest

print("Привет, мир!")
print("Ilya")
print("Ilya")

a = 5
b = 3
print(a + b)

# name = input("Введите ваше имя: ")
# print("Привет,", name)


x = 10
y = "строка"
z = 3.14
print(type(x))
print(type(y))
print(type(z))


# number = int(input("Введите число: "))
# if number > 0:
#     print("Число положительное")


for i in range(1, 6):
    print(i)


colors = ("red", "green", "blue")
print(colors[1])


person = {"name": "Иван", "age": 30}
print(person["name"])


s = {1, 2, 2, 3, 3, 3}
print(s)
print(len(s))


x = None
print(x is None)


word = "программа"
print(word[0])
print(word[7])


msg = "Python is fun"
print(msg[:6])
msg = "Python is fun"
print(msg[:9])


# f = float(input("Введите число с точкой: "))
# print(int(f))


value = 100
print(isinstance(value, int))
value = 100,5
print(isinstance(value, int))


greeting = "Привет, " + "мир!"
print(greeting)


numbers = [10, 20, 30]
numbers.remove(20)
print(numbers)


# data = {}
# data["city"] = "Москва"
# print(data)



nums = [1, 2, 2, 3, 3, 3]
unique = set(nums)
print(unique)


d = {"fruit": "яблоко"}
print(d["fruit"])


print(5 in [1, 2, 3, 4, 5])
print(6 in [1, 2, 3, 4, 5])


x = 7
print(x)


a = 10
b = 4
print(a + b)
print(a-b)
print(a * b)


print(17 // 5)
print(17 % 5)


print(2 ** 5)


x = 3
y = 7
x, y = y, x
print(x, y)


# a = int(input("Введите a: "))
# b = int(input("ВведитеВведите b: "))
# c = (a + b) * (a - b)
# print(c)


counter = 5
counter += 3
counter *= 2
print(counter)


x, y, z = 1, 2, 3
print(x + y+z)


pi = 3.14159
print(round(pi, 2))


print(5 / 2, type(5 / 2))
print(5 // 2, type(5 // 2))
print(5 / 2)


# length = float(input("Введите длину: "))
# width = float(input("Введите ширину: "))
# area = length * width
# print("Площадь :", area)


# a = float(input("Введите первое число: "))
# b = float(input("Введите второе число: "))
# c = float(input("Введите третье число: "))
# average = (a + b + c) / 3
# print("Среднее :", average)


# c = float(input("Температура в Цельсиях: "))
# f = c * 9 / 5 + 32
# print("В Фаренгейтах:", f)


# a = input("a = ")
# b = input("b = ")
# temp = a
# a = b
# b = temp
# print("a =", a, "b =", b)


# n = int(input("Введите число: "))
# if n % 2 == 0:
#     print(" Число чётное")
# else:
#     print(" Число нечётное")


# x = float(input("x = "))
# y = float(input("y = "))
# result = x ** 2 + y ** 2
# print("x² + y ² =", result)


# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
# result = (a + b) * c / 2
# print("Результат:", result)


# seconds = int(input(" Введите количество секунд: "))
# minutes = seconds // 60
# remaining = seconds % 60
# print(f"{minutes} минут и {remaining} секунд")


# number = float(input("Введите число: "))
# percent = float(input("Введите процент: "))
# result = number * percent / 100
# print("Результат:", result)


# =================================================
# from datetime import date

# d1 = input("Введите первую дату (ГГГГ-ММ-ДД): ")
# d2 = input("Введите вторую дату (ГГГГ-ММ-ДД): ")
#
# date1 = date.fromisoformat(d1)
# date2 = date.fromisoformat(d2)
#
# diff = abs((date2-date1).days)
# print("Разница в днях:", diff)
# ===================================================


# price = float(input("Введите цену товара: "))
# discount = float(input("Скидка (%): "))
# final_price = price * (1 - discount / 100)
# print("Итоговая цена :", round(final_price, 2))



# eur = float(input("Введите сумму в евро: "))
# rate = 100.25 # курс евро к рублю
# rub = eur * rate
# print("Сумма в рублях:", rub)


# weight = float(input("Вес (кг): "))
# height = float(input("Рост (м с точкой): "))
# bmi = weight / (height ** 2)
# print("BMI:", round(bmi, 2))


# credit = float(input("Сумма кредита: "))
# payment = float(input("Ежемесячный платёж :"))
# months = credit // payment
# print("Месяцев до полного погашения :", int(months))


# name = input("Введите имя: ")
# age = int(input("Введите возраст: "))
# print(f"{name}, {age} лет")


# total_minutes = int(input("Введите общее количество минут: "))
# hours = total_minutes // 60
# minutes = total_minutes % 60
# print(f"{hours} ч {minutes} мин")


# distance = float(input("Расстояние км ): "))
# consumption = float(input("Расход на 100 км л ): "))
# price = float(input("Цена за литр (руб): "))
# total = (distance / 100) * consumption * price
# print("Стоимость поездки:", round(total, 2))


# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
# result = ((a + b) ** 2 + (b-c) ** 3) / 2
# print("Результат:", round(result, 2))


# cost = float(input("Сумма покупки: "))
# given = float(input("Внесённая сумма : "))
# change = given-cost
# print("Сдача :", round(change, 2))


# num = int(input("Введите трёхзначное число: "))
# a = num // 100
# b = (num // 10) % 10
# c = num % 10
# print("Сумма цифр :", a + b + c)


#============== Окончание примеров из самостоятельной=======================


# def print_hi(param):
#     pass
#
# if __name__ == '__main__':
#     print_hi('PyCharm')

# ============================================


# Пример Теста
# Подготовка:
a, b = 2, 3
# Действие:
result = a + b
# Проверка:
assert result == 5, "Сумма должна быть 5"


# ============================================
def greet(name):
    message = "Привет, " + name
    print(message)
    return message
# Вызов функции
result = greet("Тестировщик")

# =================================================

# Простой GET тест  / См ф Python / Тесты
def test_get_users(): # Отправить запрос к открытому API
    response = requests.get("https://reqres.in/api/users")
# Проверяем статус код должен быть 200 ОК
    assert response.status_code == 200
# Преобразуем ответ в JSON
    data = response.json()
# Проверяем наличие данных
    assert "data" in data
    assert len(data["data"]) > 0
# Продолжение кода
# Проверяем структуру данных пользователя
    first_user = data ["data"][0]
    assert "id" in first_user
    assert "email" in first_user
# Проверяем конкретные значения
    assert isinstance (first_user ["id"], int)
    assert "@" in first_user ["email"]
# Выводим результат
    print ("GET-тест успешно пройден")
    print(f"Получено {len(data['data'])} пользователей")
# Запускаем тест
test_get_users ()
# =======================================


# Тест для POST запроса (создание ресурса)
def test_create_user():
# Данные для создания пользователя
    user_data = {
        "first_name": "John Doe",
        # "job": "QA Engineer"
}
# Отправляем POST запрос
    response = requests.post('https://reqres.in/api/users', json=user_data)
# Проверяем статус код (должен быть 201 Created)
    assert response.status_code == 201
# Анализируем ответ
    data = response.json()
# Продолжение кода далее
# Валидация данных в ответе  POST-запроса
# Продолжение кода
# Проверки
    assert "id" in data
    assert data["name"] == user_data["name"]
    assert data["job"] == user_data ["job"]
    assert "createdAt" in data
# Валидация времени создания
    from datetime import datetime
    created_date = datetime.strptime(data["createdAt"], "%Y Y-%m -%dT%H :%M:% fZ")
    assert created_date.year >= 2023
# Выводим результат
    print("POST POST-тест успешно пройден пройден")
    print(f"Создан пользователь: пользователь:{data['name']}, ID: {data['id']}")
# Запускаем тест
# test_create_user()
# ==================================================







