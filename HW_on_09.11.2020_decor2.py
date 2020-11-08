# Напишите декоратор для превращения функции print в генератор html-тегов
# Декоратор должен принимать список тегов italic, bold, underline
# Результатом работы декоратора с аргументами italic, bold должно быть преобразование из строки вида "test string" в "<i><b>test string</b></i>"

def str_to_html(tags):
    def decorator(func):
        tag_base = {
            "italic": f"<i>%text%</i>",
            "bold": f"<b>%text%</b>",
            "underline": f"<u>%text%</u>",
        }
        def wrapper(text):
          replace_text = text
          for tag in tags:
            replace_text = tag_base.get(tag).replace("%text%", replace_text)
          return replace_text
        return wrapper
    return decorator


# @str_to_html(["italic", "bold"])
@str_to_html(["underline", "bold"])
def get_text(text):
    return text

a = get_text('лытдыбр')
print(a)


# Напишите функцию, которая возвращает список файлов из директории.
# Напишите декоратор для этой функции, который прочитает все файлы с
# раширением .log из найденных

def log_reading(func):
    def wrapper(*args):
        for file in func(*args):
            if file[-4:] == ".log":
                f = open(file)
                print(f.read())
                f.close()
    return wrapper


@log_reading
def get_files(path):
    import os
    file_list = os.listdir(path)
    return file_list

if __name__ == '__main__':
    get_files("C:/Users/PycharmProjects/")
