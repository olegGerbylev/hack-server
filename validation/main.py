import datetime
import re


def notEmpty(value, field_name):
    if value is None or value == "":
        raise ValueError(f"Поле '{field_name}' обязательное")


def validSex(value, field_name):
    notEmpty(value,field_name)
    if value != "М" and value != "Ж":
        raise ValueError(f"Поле '{field_name}' заполнено не правильно, введите Ж или М")


def validateDate(dob, field_name):
    notEmpty(dob, field_name)
    try:
        datetime.datetime.strptime(dob, '%Y-%m-%d')
    except ValueError:
        raise ValueError(f"Поле '{field_name}' заполнено не правильно, введите дату в формате Y-m-d")


def validateEmail(email):
    notEmpty(email, 'email')
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, email):
        raise ValueError(f"Поле email заполнено не правильно, введите коректеые данные")

