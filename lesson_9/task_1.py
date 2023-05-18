"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping
будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел
должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять
их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес
сетевого узла должен создаваться с помощью функции ip_address().
"""

# воспользуемся пинг-командой со следуюшими параметрами:
'''
-w интервал

Определяет в миллисекундах время ожидания получения сообщения с эхо-ответом, 
которое соответствует сообщению с эхо-запросом. Если сообщение с эхо-ответом 
не получено в пределах заданного интервала, то выдается сообщение об ошибке 
"Request timed out". Интервал по умолчанию равен 4000 (4 секунды).

-n счетчик
Задает число отправляемых сообщений с эхо-запросом. По умолчанию - 4.
'''

from ipaddress import ip_address
from subprocess import Popen, PIPE


def host_ping(list_ip_addresses, timeout=500, requests=1):
    results = {'Доступные узлы': "", 'Недоступные узлы': ""}  # словарь с результатами
    for address in list_ip_addresses:
        try:
            address = ip_address(address)
        # обойдем такие исключения
        # ValueError: 'yandex.ru' does not appear to be an IPv4 or IPv6 address
        # хотя можно преобразовать доменное имя к ip-адресу
        except ValueError:
            pass
        proc = Popen(f"ping {address} -w {timeout} -n {requests}", shell=False, stdout=PIPE)
        proc.wait()
        # проверяем код завершения подпроцесса
        if proc.returncode == 0:
            results['Доступные узлы'] += f"{str(address)}\n"
            res_string = f'{address} - Узел доступен'
        else:
            results['Недоступные узлы'] += f"{str(address)}\n"
            res_string = f'{address} - Узел недоступен'
        print(res_string)
    return results


if __name__ == '__main__':
    ip_addresses = ['yandex.ru', '2.2.2.2', '192.168.0.100', '192.168.0.101']
    host_ping(ip_addresses)

"""
Результат:

yandex.ru - Узел доступен
2.2.2.2 - Узел недоступен
192.168.0.100 - Узел доступен
192.168.0.101 - Узел недоступен
"""


#Мой вариант(нейро сеть)
# import subprocess
# from ipaddress import ip_address
#
# def host_ping(hosts):
#     for host in hosts:
#         try:
#             ip = ip_address(host)
#         except ValueError:
#             print(f"Invalid address: {host}")
#             continue
#         ping_cmd = f"ping {str(ip)} -n 1"
#         try:
#             output = subprocess.check_output(ping_cmd, shell=True, universal_newlines=True)
#             if "Reply" in output:
#                 print(f"{host} is available.")
#             elif "timed out" in output:
#                 print(f"{host} is not available.")
#             else:
#                 print(f"Unknown error: {output}")
#         except subprocess.CalledProcessError as e:
#             print(f"Error pinging {host}: {e}")
#
#
# if __name__ == '__main__':
#     ip_addresses = ['yandex.ru', '2.2.2.2', '192.168.0.100', '192.168.0.101']
#     host_ping(ip_addresses)