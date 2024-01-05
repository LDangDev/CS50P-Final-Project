import requests, sys
from tabulate import tabulate
from datetime import date, datetime


def main():
    while True:
        city_name = input("Which city you wanna check the temperature: ").strip()
        data = call_api(city_name, "")
        if data["cod"] == 200 and check_valid_input(city_name):
            while True:
                unit = input("Do you prefer °C or °F (C/F): ").upper()
                if check_valid_unit(unit):
                    data = call_api(city_name, unit)
                    city_name = data["name"]
                    country_code = data["sys"]["country"]
                    temp = round(data["main"]["temp"])
                    temp_max = round(data["main"]["temp_max"])
                    temp_min = round(data["main"]["temp_min"])
                    feel_like = round(data["main"]["feels_like"])
                    wind_speed = round(data["wind"]["speed"])
                    today = get_date()
                    time = get_time()
                    if unit == "C":
                        headers = [
                            "Time",
                            "Date",
                            "City",
                            "Country Code",
                            "Temp (°C)",
                            "Feel like",
                            "Max Temp",
                            "Min Temp",
                            "Wind Speed (m/s)",
                        ]
                    else:
                        headers = [
                            "Time",
                            "Date",
                            "City",
                            "Country Code",
                            "Temp (°F)",
                            "Feel like",
                            "Max Temp",
                            "Min Temp",
                            "Wind Speed (m/s)",
                        ]

                    table_data = [
                        [
                            time,
                            today,
                            city_name,
                            country_code,
                            temp,
                            feel_like,
                            temp_max,
                            temp_min,
                            wind_speed,
                        ]
                    ]

                    print(tabulate(table_data, headers, tablefmt="pretty"))
                    sys.exit("Exiting program...")
                else:
                    print("Invalid choice")
                    pass
        else:
            print("Invalid city name! Please try again!")
            print("---------------------------------------------------------\n")
            pass


def call_api(input, unit):
    if unit == "C":
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={input}&appid=cf9b18c313529565bde1114489b7b076&units=metric"
    else:
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={input}&appid=cf9b18c313529565bde1114489b7b076&units=imperial"

    response = requests.get(api_url)
    data = response.json()

    return data


def check_valid_input(input):
    if input.isdigit():
        return False
    return True


def check_valid_unit(unit):
    if unit.upper() == "C" or unit.upper() == "F":
        return True
    return False


def get_date():
    today = str(date.today())
    year, month, day = today.split("-")
    today_display = f"{day}/{month}/{year}"

    return today_display


def get_time():
    time = datetime.now()
    hour = time.hour
    minutes = time.minute
    if hour >= 0 and hour <= 9 or minutes >= 0 and minutes <= 9:
        time_display = f"{hour:02d}:{minutes:02d}"
    else:
        time_display = f"{hour}:{time}"

    return time_display


if __name__ == "__main__":
    main()
