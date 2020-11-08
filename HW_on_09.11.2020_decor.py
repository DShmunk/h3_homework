# Написать свой cache декоратор c максимальным размером кеша и его очисткой при необходимости.
# Декоратор должен перехватывать аргументы оборачиваемой функции
# Декоратор должен иметь хранилище, где будут сохраняться все перехваченные аргументы и результаты выполнения декорируемой функции
# Декоратор должен проверять наличие перехваченных аргументов в хранилище. Если декорируемая функция уже вызывалась с такими аргументами,
#   она не будет вызываться снова, вместо этого декоратор вернет сохраненное значение.
# Декоратор должен принимать один аргумент - максимальный размер хранилища.
# Если хранилище заполнено, нужно удалить 1 любой элемент, чтобы освободить место под новый.

def do_cache(maxsize):
  # в роли хранилища dict {(аргументы): значения ф-ии, }
  cache = dict()
  def cached(get_value):
    def cached_func(*args):
      if args in cache:
        return cache[args]
      result = get_value(*args)
      if len(cache) == maxsize:
        cache.popitem()
      cache[args] = result
      print(cache)
      return result
    return cached_func
  return cached


@do_cache(maxsize=3)
def get_value(a, b):
  return a ** b


sss = get_value(1, 4)
print(sss)

sss = get_value(2, 4)
print(sss)

sss = get_value(3, 4)
print(sss)

sss = get_value(4, 4)
print(sss)

sss = get_value(4, 4)
print(sss)

