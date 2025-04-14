import requests
from bs4 import BeautifulSoup


def get_weather_google(city: str):
    url = f"https://www.google.com/search?q=погода+{city}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    try:
        temperature = soup.find("span", id="wob_tm").text
        condition = soup.find("span", id="wob_dc").text
        humidity = soup.find("span", id="wob_hm").text

        print(f"🌆 Google - {city.capitalize()}")
        print(f"🌡 Температура: {temperature}°C")
        print(f"📖 Описание: {condition}")
        print(f"💧 Влажность: {humidity}")
    except AttributeError:
        print("⚠️ Не удалось получить данные с Google.")


def get_weather_yandex(city: str):
    url = f"https://yandex.ru/pogoda/{city.lower()}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    try:
        temp = soup.find("span", class_="temp__value").text
        condition = soup.find("div", class_="link__condition").text

        print(f"🌆 Яндекс - {city.capitalize()}")
        print(f"🌡 Температура: {temp}°C")
        print(f"📖 Описание: {condition}")
    except AttributeError:
        print("⚠️ Не удалось получить данные с Яндекса.")


def get_weather_gismeteo(city: str):
    url = f"https://www.gismeteo.ru/weather-{city.lower()}/"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    try:
        temp = soup.find("span", class_="unit_temperature_c").text
        condition = soup.find("div", class_="weather-value").text

        print(f"🌆 Gismeteo - {city.capitalize()}")
        print(f"🌡 Температура: {temp}")
        print(f"📖 Описание: {condition}")
    except AttributeError:
        print("⚠️ Не удалось получить данные с Gismeteo.")


if __name__ == "__main__":
    city = input("Введите город (например: moscow, kazan): ").strip().lower()
    print("Выберите источник:")
    print("1 - Google")
    print("2 - Яндекс")
    print("3 - Gismeteo")
    choice = input("Ваш выбор (1/2/3): ")

    if choice == "1":
        get_weather_google(city)
    elif choice == "2":
        get_weather_yandex(city)
    elif choice == "3":
        get_weather_gismeteo(city)
    else:
        print("Неверный выбор.")