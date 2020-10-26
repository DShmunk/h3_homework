# def catalog_finder(url_list):
#     """
#     Дописать функцию, которая принимает список URL, а возвращает
#     список только тех URL, в которых есть /catalog/
#     """
#     # your code here
#     result_list = None
#     return result_list

def catalog_finder(url_list):
    result_list = [eachURL for eachURL in url_list if '/catalog/' in eachURL]
    # print(result_list)
    return result_list

# # пример
# url_list = ('https://www.google.com/search?jkjhf', 'https://wikipedia.org/wiki/catalog', 'https://www.python.org/catalog/')
# catalog_finder(url_list)




# def get_str_center(input_str):
#     """
#     Дописать функцию, которая вернет Х символов из середины строки
#     (2 для четного кол-ва символов, 3 - для нечетного).
#     """
#     # your code here
#     output_str = None
#     return output_str

def get_str_center(input_str):
    middleOfStr = len(input_str)//2
    # totalLen = len(input_str)
    if len(input_str) % 2 == 0:
        output_str = input_str[middleOfStr - 1 : middleOfStr + 1]
    else:
        output_str = input_str[middleOfStr - 1 : middleOfStr + 2]
    print(output_str)
    return output_str

# #строка с четным к-вом
# input_string1 = 'dddwww'
# get_str_center(input_string1)
#
# #строка с нечетным к-вом
# input_string2 = 'dddrrrwww'
# get_str_center(input_string2)




# def count_symbols(input_str):
#     """
#     Дописать функцию, которая считает сколько раз каждая из букв
#     встречается в строке, разложить буквы в словарь парами
#     {буква:количество упоминаний в строке}
#     """
#     # your code here
#     output_dict = None
#     return output_dict

def count_symbols(input_str):
    output_dict = {}
    for i in input_str:
        if i in output_dict:
            output_dict[i] += 1
        else:
            output_dict[i] = 1
    return output_dict

# input_string1 = 'best day to die'
# result1 = count_symbols(input_string1)
# print(result1)




# def mix_strings(str1, str2):
#     """
#     Дописать функцию, которая будет принимать 2 строки и вставлять вторую
#     в середину первой
#     """
#     # your code here
#     result_str = None
#     return result_str

def mix_strings(str1, str2):
    middleOfStr1=len(str1)//2
    result_str = str1[:middleOfStr1] + str2 + str1[middleOfStr1:]
    # print(result_str)
## вариант конкатенации, но в >2 раза медленнее
    # result_str2 = "{0}{1}{2}".format(str1[:middleOfStr1], str2, str1[middleOfStr1:])
    # print(result_str)
    return result_str

# #строка с четным к-вом
# string1 = 'dddwww'
# string2 = '___'
# mix_strings(string1, string2)
#
# #строка с нечетным к-вом
# string3='dddrrrwww'
# string2='___'
# mix_strings(string3, string2)




# def even_int_generator():
#     """
#     Сгенерировать список из диапазона чисел от 0 до 100 и записать
#     в результирующий список только четные числа.
#     """
#     # your code here
#     even_int_list = None
#     return even_int_list

def even_int_generator():
    even_int_list = [gener_num for gener_num in range(0,100) if gener_num % 2 == 0]
    return even_int_list
