from flask import request, jsonify, g
import psycopg2
import psycopg2.extras
import validation.main as validation
from helper.hash import hash_password, verify_password
from helper.generateToken import generate_unique_token


def register():
    db = g.db
    cursor = db.cursor()

    try:
        # Данные о пользователе
        name = request.json.get('name')
        validation.notEmpty(name, 'Имя')
        familyName = request.json.get('familyName')
        validation.notEmpty(familyName, "Фамилия")
        surname = request.json.get('surname')
        validation.notEmpty(surname, "Отчество")
        sex = request.json.get('sex')
        validation.validSex(sex, "пол")
        DOB = request.json.get('DOB')
        validation.validateDate(DOB, "дата рождения")

        # Данные для регистрации
        email = request.json.get('email')
        validation.validateEmail(email)
        password = request.json.get('password')
        validation.notEmpty(password, "password")
        password = hash_password(password)

        # Данные о компании
        company = request.json.get('company')
        validation.notEmpty(company, 'company')
        companyTIN = request.json.get('companyTIN')
        validation.notEmpty(companyTIN, 'ИНН компании')

        # Паспортные данные
        passportSeries = request.json.get('passportSeries')
        validation.notEmpty(passportSeries, 'серия паспорта')
        passportID = request.json.get('passportID')
        validation.notEmpty(passportID, 'номер паспорта')
        issuedBy = request.json.get('issuedBy')
        validation.notEmpty(issuedBy, 'кем выдан')
        dateIssue = request.json.get('dateIssue')
        validation.validateDate(dateIssue, 'дата выдачи')
        departmentCode = request.json.get('departmentCode')
        validation.notEmpty(departmentCode, 'код департамента')
        location = request.json.get('location')
        validation.notEmpty(location, 'прописка')

        PPD = request.json.get('PPD')
        if PPD != 'true':
            return jsonify({'error': 'Дайте согласие на обработку персональныз данных'}), 401

    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    try:
        cursor.execute('''INSERT INTO users (token ,email, password, name, family_name, surname, sex, dob, company, 
        company_tin, passport_series, passport_id, issued_by, date_issue, department_code, location, ppd) VALUES (%s, %s, 
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                       (generate_unique_token(), email, password, name, familyName, surname, sex, DOB, company, companyTIN, passportSeries,
                        passportID, issuedBy, dateIssue, departmentCode, location, True))
        db.commit()
        return jsonify({'message': 'Пользователь успешно зарегистрирован'})
    except psycopg2.Error as e:
        db.rollback()
        return jsonify({'error': 'Произошла ошибка при регистрации пользователя'}), 500
    finally:
        cursor.close()


def login():
    db = g.db
    cursor = db.cursor(
        cursor_factory=psycopg2.extras.RealDictCursor)

    email = request.json.get('email')
    password = request.json.get('password')


    cursor.execute('SELECT token ,email, password, name, family_name, surname, sex, dob, company, company_tin, passport_series, passport_id, issued_by, date_issue, department_code, location, ppd FROM users WHERE email = %s', (email,))
    user = cursor.fetchone()

    if user is None:
        return jsonify({'error': 'Неверные учетные данные'}), 401

    if not verify_password(password, user['password']):
        return jsonify({'error': 'Неверные учетные данные'}), 401

    return jsonify({'message': 'Успешный вход', 'user_id': user['token']})
