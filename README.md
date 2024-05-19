# Real time weather condition info

#### Description:
#### This Python program allows user to check real-time weather data for any valid city of their choice and display it in either °C (Celsius) or °F (Fahrenheit) degree. The program retrieves weather information from the [OpenWeatherMap API](https://openweathermap.org/current#data).
**Note:** This program is non-sensitive to case. It will accept both upper and lower case inputs as long as valid choice or city name for unit selection (°C or °F) and city names.
#### Table of Contents

1. [How to Use](#how-to-use)
2. [Dependencies](#dependencies)
3. [API Key](#api-key)
4. [Unit Selection](#unit-selection)
5. [Functionality](#functionality)
6. [Testing](#testing)

#### [1. How to use](#1-how-to-use)
Clone or download this repository to your local machine.

Open your terminal or command prompt and navigate to the project directory.

Run the program by executing the following command:
```
python project.py
```
#### [2. Dependencies](#dependencies)
The program uses the following Python libraries:

`requests` for making HTTP requests to the OpenWeatherMap API.

`tabulate` for formatting and displaying the weather data in a table.

`datetime` for date and time information.

#### [3. API Key](#3-api-key)
The program uses the [OpenWeatherMap API](https://openweathermap.org/current#data) to fetch weather data. To use the API, you need to obtain an API key from OpenWeatherMap.

Once you have your API key, replace the placeholder {API key} with your actual API key in the call_api function in the project.py file.

#### [4. Unit Selection](#4-unit-selection)
You can choose to display the temperature in either °C (Celsius) or °F (Fahrenheit) by entering 'C' or 'F' when prompted. The program will display the data accordingly.

#### [5. Functionality](#5-functionality)
It prompts you to enter the city you want to check weather condition for.

It validates the city name to ensure it's not a sequence of digits or invalid name as the API may return results errors

You can select the temperature unit (°C or °F).

The program calls the OpenWeatherMap API with the city name and temperature unit to fetch real-time weather data.

It formats the weather data into a table and displays it on the screen, including information such as temperature, feel-like temperature, maximum temperature, minimum temperature, wind speed, city name, country code, date, and time.
The real time and date will be formatted HH:MM and DD/MM/YYYY, respectively

#### [6. Testing](#6-testing)
Unit tests are provided for all functions in the project.py except the main() function, and pytest is used as the testing framework.
Run the following command to run the test:
```
pytest test_project.py
```

If you encounter any issues or have suggestions for improvements in the testing process, please let me know.
