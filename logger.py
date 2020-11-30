'''
Используйте этот код, чтобы создать импортируемый модуль logger.
Подключите логирование во все классы ORM.
Точки логирования и тексты - на ваше усмотрение.
'''
import logging


class MyLogger(logging.Logger):
    def __init__(self, name):
        super().__init__(name)
        # добавил логирование времени события
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        # ch изменил на sh (было замечание в лекции)
        sh = logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        sh.setFormatter(formatter)
        self.addHandler(sh)

        # advanced_log.log изменил на advanced.log
        fh = logging.FileHandler('advanced.log')
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)
        self.addHandler(fh)