from datetime import date
# d = date(1969, 6, 26) - конструктор даты
# d.year < 2020 - проверка даты

# database - список словарей, эмулирующий базу данных со строками и полями
database = list()

def _validate_input(data: tuple) -> bool:
    """
    Функция принимает кортеж словарей, валидирует каждый из словарей на наличие
    всех необходимых полей и тип их данных. Возвращает bool в зависимости от результатов проверки.
    Правила валидации:
    first_name - string, не пустой, короче 48 символов
    last_name - string, не пустой, короче 64 символов
    birth - date, не пустой, не в будущем, не старше 100 лет
    email - string, формат строка, затем @, затем опять строка, точка,
    строка от 2 до 3 символов
    Допустимые символы в email: буквы, цифры
    """
    first_name_len = 48
    last_name_len = 64
    max_age = 100
    for row in data:
        if not _validate_name(row['first_name'], first_name_len):
            return False
        if not _validate_name(row['last_name'], last_name_len):
            return False
        if not _validate_birth(row['birth'], max_age):
            return False
        if not _validate_email(row['email']):
            return False
    return True


def _validate_name(name, max_len):
    if not type(name) is str:
        return False
    if not 0 < len(name) < max_len:
        return False
    return True


def _validate_birth(birth, max_age):
    if not type(birth) is date:
        return False
    if birth > date.today():
        return False
    if date.today().year - birth.year > max_age:
        return False
    return True


def _validate_email(email):
    if not type(email) is str:
        return False
    email_parts = email.split('@')
    if len(email_parts) != 2:
        return False
    if not email_parts[0].isalnum():
        return False
    domain_parts = email_parts[1].split('.')
    if len(domain_parts) == 1:
        return False
    if not 2 <= len(domain_parts[-1]) <= 3:
        return False
    return True


def insert_to_db(data: tuple) -> bool:
    """
    Функция принимает кортеж словарей с данными, валидирует каждую запись с
    помощью вспомогательной функции validate_input, и если данные валидны,
    добавляет их в database.
    Возвращает bool по результатам успешного/неуспешного выполнения.
    """
    if _validate_input(data):
        database.extend(list(data))
        return True
    return False


def _format_output(data):
    """
    Принимает тапл диктов с данными из БД.
    Форматирует данные в таблицу вида:
    ---------------------------------------
    | название колонки | название колонки |
    ---------------------------------------
    | значение строки  | значение колонки |
    Возвращает таблицу строкой.
    """
    # из условия знаем,что в базе 4 поля и знаем их названия.
    # в связи с тем, что порог отсечки полей по размеру весьма велик,
    # есть смысл делать поля по размеру значений данных,
    # но не <10, чтобы не мельчить.
    # + замыкающая линия - при печати видно, где конец таблицы.
    # определяемся с размером полей:
    first_name_len = max(list(map(lambda x: len(x['first_name']), data)))
    last_name_len = max(list(map(lambda x: len(x['last_name']), data)))
    email_len = max(list(map(lambda x: len(x['email']), data)))
    birth_len = 10
    if first_name_len < 10: first_name_len = 10
    if last_name_len < 10:  last_name_len = 10
    if email_len < 10:      email_len = 10
    table = ""
    # длина разделительной линии: +2 вначале, +2 в конце, +3*3 внутри = 13
    terminator = "{0}{1}".format('-'*(first_name_len + last_name_len + birth_len + email_len), '-' * 13)
        # если бы выравнивание было одинаковым, напр.по 10:
        # head_lines = list()
        # for element in list(data[0].keys()):
        #     head_lines.append(element.ljust(10) + ' | ')
        # headline = f"| {''.join(head_lines)}\n"
    # 4 элемента названия дописываем до макс.длины значения столбца
    head_lines = list()
    head_lines.append(list(data[0].keys())[0].ljust(first_name_len) + ' | ')
    head_lines.append(list(data[0].keys())[1].ljust(last_name_len) + ' | ')
    head_lines.append(list(data[0].keys())[2].ljust(birth_len) + ' | ')
    head_lines.append(list(data[0].keys())[3].ljust(email_len) + ' |')
    headline = f"| {''.join(head_lines)}"
    # набор данных для тела таблицы
    data_list = list()
    for data_dict in data:
        data_list.append('| ')
        data_list.append(list(data_dict.values())[0].ljust(first_name_len) + ' | ')
        data_list.append(list(data_dict.values())[1].ljust(last_name_len) + ' | ')
        data_list.append(list(data_dict.values())[2].strftime("%m.%d.%Y").ljust(birth_len) + ' | ')
        data_list.append(list(data_dict.values())[3].ljust(email_len) + ' |' + '\n')
        data_table = f"{''.join(data_list)}"
    table = "{0}{1}{2}{1}{0}{1}{3}{0}".format(terminator, '\n', headline, data_table)
    return table


def select_from_db(field, value):
    """
    Функция возвращает таблицу (строка) с релевантными результатами, где переданное значение встречается в переданном ключе.
    Форматирование результатов выполняет вспомогательная функция _format_output
    """
    selected_dicts = list()
    selected_dicts = [d for d in database if d[field] == value]
    # сообщение на случай отсутствия данных
    if selected_dicts == []:
        print('Items not found in DB!')
        return ""
    return _format_output(selected_dicts)




in_data = ({"first_name": "Guido", "last_name": "Van Rossum",
            "birth": date(1969, 6, 27), "email": "iamguido@python.org"},
            {"first_name": "Jon", "last_name": "Snow",
            "birth": date(1945, 5, 18), "email": "youknownothingjonsnow@got.tv"},
           {"first_name": "Elon", "last_name": "Musk",
            "birth": date(1971, 6, 28), "email": "elonmusk@spacex.com"},
           {"first_name": "John", "last_name": "Wick",
            "birth": date(1943, 1, 1), "email": "chapter4@lionsgate.com"},
           {"first_name": "John", "last_name": "Washington",
            "birth": date(1930, 12, 12), "email": "lastwar@usa.org"},
            {"first_name": "Jon", "last_name": "Livingston",
            "birth": date(1950, 7, 7), "email": "jonatan@oldscool.com"})
result = insert_to_db(in_data)
print(result)
print(database)

result2 = select_from_db("first_name", "John")
print(result2)
result2 = select_from_db("first_name", "Jon")
print(result2)
result2 = select_from_db("first_name", "Jo")
print(result2)