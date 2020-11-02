def validate_password(password):
    """
    Функция принимает пароль строкой и выполняет валидацию с помощью трёх
    вспомогательных функций:
    1. Содержит только a−z, A−Z, 0−9
    2. Содержит четное количество букв
    3. Содержит нечетное количество цифр
    Основная функция возвращает True, если пароль валидный.
    Если пароль не валидный, возвращает лист стрингов, в которых перечислены
    причины неуспешной проверки. Например: ["содержит запрещенные символы"]
    """
    check_funcs_list = [_validate_symbols, _validate_letters_even, _validate_numbers_odd]
    errors_list = list()
    for func in check_funcs_list:
        result = func(password)
        if result == True:
            continue
        else:
            errors_list.append(result)
    if errors_list:
        return errors_list
    else:
        return True
# прогнать циклом каждую ф-ю и добавить в лист errors_list ошибки


def _validate_symbols(input_str):
  """
  Проверяет строку на наличие запрещенных символов
  Подсказка: у строк есть метод, проверяющий наличие только був и цифр
  Возвращает True\False
  """
  if input_str.isalnum():
      if input_str.isascii():
          return True
  return 'содержит запрещенные символы'
  #  isalnum - метод, проверяющий наличие букв и цифр, isascii - на ascii; их сочетание убирает знаки ascii


def _validate_letters_even(input_str):
  """
  Проверяет строку на четное количество букв
  Возвращает True\False
  """
  letters = ''
  for passchar in input_str:
      if passchar.isalpha():
          letters += passchar
  if len(letters) % 2 or len(letters) == 0:
      return 'нечетное количество букв или их отсутствие'
  else:
      return True
# isalpha - метод проверки содержания букв


def _validate_numbers_odd(input_str):
  """
  Проверяет строку на нечетное количество цифр
  Возвращает True\False
  """
  numbers = ''
  for passchar in input_str:
      if passchar.isdigit():
          numbers += passchar
  if len(numbers) % 2:
      return True
  else:
      return 'четное количество цифр или их отсутствие'
# isdigit - метод проверки содержания цифр


password = "дихлордифенилтрихлорметилметан"
print(validate_password(password))

password = "666"
print(validate_password(password))

password = "pass666"
print(validate_password(password))