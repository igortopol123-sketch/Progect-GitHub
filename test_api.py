import requests
# import pytest


# Делаем GET запрос к публичному API
def test_get_inventory():
    response = requests.get("https://petstore.swagger.io/v2/store/inventory")
# Выводим статус код и данные
    print("Статус:", response.status_code)
    print("Данные:", response.json())
# ============================================


# def test_get_inventory():
    response = requests.get("https://petstore.swagger.io/v2/store/inventory")

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    data = response.json()
    print("Данные:", data)

    assert isinstance(data, dict), "Response should be a dictionary"
    assert len(data) > 0, "Inventory should not be empty"


    response = requests.get("https://petstore.swagger.io/v2/store/inventory")
# Проверяем, что сервер ответил успешно (статус 200)
    assert response.status_code == 200, "Статус не 200!"
# Проверяем, что в ответе есть поле "available"
    data = response.json()
    assert 'available' in data, "В ответе есть поле 'available'!"
    print("✅ Тест пройден!")

