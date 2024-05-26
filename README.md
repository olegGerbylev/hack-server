# Клиентский портал по исследованию защищенности внешнего периметра заказчика

### 2. Описание проекта
Этот проект предназначен для для проверки прав юридического лица на подписание документов. Портал предоставляет возможность провести аутентификацию клиента, чтобы убедиться в легальности подписывающего лица. Сервис включает функционал для обработки и проверки документов с электронной цифровой подписью (ЭЦП) через API Госуслуг.

### 3.  Юридическая информация
1. Этот проект использует и обрабатывает персональные данные в соответствии с [Политикой обработки персональных данных в ПАО «МТС».](https://moskva.mts.ru/about/investoram-i-akcioneram/korporativnoe-upravlenie/dokumenti-pao-mts/politika-obrabotka-personalnih-dannih-v-pao-mts) Пользователи обязаны ознакомиться с этой политикой и дать согласие на обработку своих данных в процессе регистрации и использования сервиса (статья 152 ФЗ)

### Политика обработки персональных данных

1. **Обработка персональных данных**:
   - Все персональные данные обрабатываются в строгом соответствии с [Политикой обработки персональных данных в ПАО «МТС»](https://moskva.mts.ru/about/investoram-i-akcioneram/korporativnoe-upravlenie/dokumenti-pao-mts/politika-obrabotka-personalnih-dannih-v-pao-mts).
   - Политика включает положения о сборе, использовании, хранении и защите персональных данных пользователей.

2. **Согласие пользователя**:
   - При регистрации в сервисе пользователи должны подтвердить свое согласие на обработку их персональных данных.
   - Согласие выражается путем акцепта условий [Политики обработки персональных данных в ПАО «МТС»](https://moskva.mts.ru/about/investoram-i-akcioneram/korporativnoe-upravlenie/dokumenti-pao-mts/politika-obrabotka-personalnih-dannih-v-pao-mts), с которой пользователь обязан ознакомиться перед регистрацией.

3. **Цель обработки персональных данных**:
   - Персональные данные собираются и обрабатываются для обеспечения функциональности сервиса управления уязвимостями и отслеживания киберугроз.
   - Данные могут использоваться для аутентификации пользователей, предоставления доступа к сервису, анализа и обработки уязвимостей, а также для связи с пользователями.

4. **Передача данных**:
   - Персональные данные могут передаваться третьим лицам только в рамках, предусмотренных законодательством Российской Федерации и [Политикой обработки персональных данных в ПАО «МТС»](https://moskva.mts.ru/about/investoram-i-akcioneram/korporativnoe-upravlenie/dokumenti-pao-mts/politika-obrabotka-personalnih-dannih-v-pao-mts).
   - В случае передачи данных третьим лицам, все они обязуются соблюдать конфиденциальность и обеспечивать защиту персональных данных.

5. **Права пользователей**:
   - Пользователи имеют право на доступ к своим персональным данным, их корректировку, удаление и ограничение обработки.
   - Для реализации своих прав пользователи могут обратиться в службу поддержки проекта.

### Авторизационное письмо
Шаблон авторизационного письма составлен в соответствии с регламентом ФСТЭК по организации электронного документооборота и использования ЭЦП. Подписывая авторизационное письмо клиет подтверждает что лицо, указанное в данном авторизационном письме может представлять интересы компании и обладает рядом  полномочий, описанных в авторизационном письме

### Проверка электронной подписи

Проверка электронной цифровой подписи (ЭЦП) осуществляется с использованием официального API Портала государственных услуг Российской Федерации. Это гарантирует, что все подписанные документы соответствуют требованиям действующего законодательства и проверяются на подлинность с использованием надежного и авторитетного источника.

#### Процесс проверки ЭЦП:

1. **Загрузка документа с ЭЦП**:
   - Пользователь загружает документ, подписанный ЭЦП, через интерфейс сервиса.

2. **Валидация документа**:
   - Сервис сравнивает загруженный документ с исходным документом, отправленным пользователю, чтобы убедиться, что в нем не было внесено никаких изменений, кроме добавления ЭЦП.

3. **Проверка подлинности ЭЦП**:
   - Для проверки подлинности ЭЦП используется API Портала государственных услуг Российской Федерации. Этот процесс включает:
     - Отправку документа с ЭЦП на проверку через API.
     - Получение ответа от API, подтверждающего подлинность или недействительность ЭЦП.

4. **Уведомление пользователя**:
   - После проверки пользователь уведомляется о результате проверки ЭЦП. Если подпись действительна и документ не был изменен, документ считается подтвержденным и принимается к обработке.


### 4. Установка
#### Предварительные требования
- Python 3.8+
- PostgreSQL

#### Шаги установки
1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/olegGerbylev/hack-server.git
    cd cicada8-service
    ```

2. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```

3. Настройте базу данных:
    ```sh
    psql -U youruser -d yourdb -f migrations/V1__init.sql
    ```

### 5. Использование
Запустите основной файл для старта сервиса:
```sh
python main.py
```

### 6. Структура проекта
- `document/` - Каталог для исходных и возвращенных документов.
- `helper/` - Вспомогательные функции и скрипты.
- `migrations/` - Скрипты для инициализации и миграции базы данных.
- `service/` - Основная логика сервиса.
  - `auth.py` - Модуль аутентификации.
  - `file.py` - Модуль для работы с файлами.
  - `sender.py` - Модуль для отправки данных.
  - `validation/` - Модули для валидации данных.
    - `main.py` - Основной файл для валидации.
- `db.py` - Конфигурация базы данных.
- `main.py` - Главный файл для запуска сервиса.

### 7. Конфигурация
```python
DATABASE = {
    'host': 'localhost',
    'port': 5432,
    'user': 'youruser',
    'password': 'yourpassword',
    'dbname': 'yourdb'
}

API_GOSUSLUGI = {
    'url': 'https://api.gosuslugi.ru/verify_ecp',
    'token': 'your_api_token'
}
```

### 8. Тестирование
Для тестирования используйте встроенные функции и библиотеки:
```sh
pytest
```

### 9. Вклад в проект
Если вы хотите внести вклад в проект, пожалуйста, следуйте этим шагам:
1. Сделайте форк репозитория.
2. Создайте новую ветку (`git checkout -b feature/AmazingFeature`).
3. Сделайте коммит ваших изменений (`git commit -m 'Add some AmazingFeature'`).
4. Отправьте изменения (`git push origin feature/AmazingFeature`).
5. Откройте Pull Request.

### 10. Лицензия
Этот проект лицензирован под лицензией MIT. Подробности смотрите в файле [LICENSE](LICENSE).