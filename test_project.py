from project import call_api, check_valid_input, check_valid_unit, get_date, get_time
import requests
from datetime import datetime


def test_call_api_Celsius():
    data = call_api("helsinki", "C")

    assert data["cod"] == 200
    assert data["name"] == "Helsinki"


def test_call_api_Fahrenheit():
    data = call_api("helsinki", "F")

    assert data["cod"] == 200
    assert data["name"] == "Helsinki"


def test_check_valid_input():
    assert check_valid_input("0909") == False
    assert check_valid_input("helsink12") == True
    assert check_valid_input("helsinki@") == True


def test_check_valid_unit():
    assert check_valid_unit("C") == True
    assert check_valid_unit("F") == True
    assert check_valid_unit("") == False
    assert check_valid_unit("324") == False
    assert check_valid_unit("#@$@#$") == False


def test_get_date():
    today_str = get_date()
    formatted_date_str = datetime.today().strftime("%d/%m/%Y")
    assert formatted_date_str == today_str


def test_get_time():
    time_str = get_time()
    formatted_time_str = datetime.now().strftime("%H:%M")
    assert time_str == formatted_time_str
