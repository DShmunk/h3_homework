'''У вас есть список(list) IP адрессов. Вам необходимо создать
класс который сможет:
1) Получить и изменить список IP адресов
2) Получить список IP адресов в развернутом виде
(10.11.12.13 -> 13.12.11.10)
3) Получить список IP адресов без первых октетов
(10.11.12.13 -> 11.12.13)
4) Получить список последних октетов IP адресов
(10.11.12.13 -> 13)'''


class IpHandler:
    """Handles a list of IPs, each IP must be a string"""
    def __init__(self, ip_list):
        self._ip_list = ip_list

    @property
    # в условии название ф-ии было "ipList". В 1й ДЗ было замечание, что названия ф-й с заглавными недопустимы.
    # Изменил на "ip_list"
    def ip_list(self):
        return self._ip_list

    @ip_list.setter
    # newList изменил на new_list
    def ip_list(self, new_list):
        self._ip_list = new_list

    def reverse_ip(self):
        """Return it's IPs reversed"""
        result = list()
        for each_ip in self._ip_list:
            splitted_ip = each_ip.split('.')
            new_ip = '.'.join(reversed(splitted_ip))
            # new_ip = '.'.join(splitted_ip[::-1]) - первый вариант, не принят по принципу "метод лучше сплита"
            result.append(new_ip)
        return result

    def get_oct_1_3(self):
        """Returns a list of IPs without first octets (127.0.0.1 -> .0.0.1)"""
        result = list()
        for each_ip in self._ip_list:
            splitted_ip = each_ip.split('.')
            new_ip = '.'.join(splitted_ip[1:])
            result.append(new_ip)
        return result

    def get_oct_3(self):
        """Returns a list of last octets of each IP (127.0.0.1 -> .1)"""
        # конфликт задач - выполнено по заглавному заданию (без точки)
        result = list()
        for each_ip in self._ip_list:
            splitted_ip = each_ip.split('.')
            new_ip = f'{splitted_ip[3:][0]}'
            result.append(new_ip)
        return result

if __name__ == '__main__':
    ip_list = ['10.11.12.13', '127.0.0.1', '127.0.0.2', '666.666.666.13']
    handler = IpHandler(ip_list = ip_list)
    # print(handler.reverse_ip())
    # print(handler.get_oct_1_3())
    # print(handler.get_oct_3())


'''Создайте класс который будет хранить параметры для
подключения к физическому юниту (например сервер). В своем
списке атрибутов он должен иметь минимальный набор
(unit_name, mac_address, ip_address, login, password).
Вы должны описать каждый из этих атрибутов в виде гетеров и
сеттеров (@property). У вас должна быть возможность
получения и назначения этих атрибутов в классе.'''


class ConnHandler:
    __slots__ = ['_unit_name', '_mac_address', '_ip_address', '_login', '_password']

    def __init__(self, unit_name='', mac_address='', ip_address='', login='', password=''):
        self._unit_name = unit_name
        self._mac_address = mac_address
        self._ip_address = ip_address
        self._login = login
        self._password = password

    @property
    def unit_name(self):
        return self._unit_name

    @property
    def mac_address(self):
        return self._mac_address

    @property
    def ip_address(self):
        return self._ip_address

    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return self._password

    @unit_name.setter
    def unit_name(self, new_name):
        self._unit_name = new_name

    @mac_address.setter
    def mac_address(self, new_mac_address):
        self._mac_address = new_mac_address

    @ip_address.setter
    def ip_address(self, new_ip_address):
        self._ip_address = new_ip_address

    @login.setter
    def login(self, new_login):
        self._login = new_login

    @password.setter
    def password(self, new_password):
        self._password = new_password

if __name__ == '__main__':
    unit_name='qwerty'
    mac_address='3.14.15.92.6'
    ip_address='322.223.322'
    login='login'
    password='password'
    handler = ConnHandler(unit_name = unit_name,
                          mac_address = mac_address,
                          ip_address = ip_address,
                          login = login,
                          password = password)
    # print(handler.unit_name)