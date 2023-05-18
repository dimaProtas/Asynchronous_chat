import socket
import threading

# создаем объект серверного сокета
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# связываем серверный сокет с хостом и портом
server_socket.bind(('localhost', 8888))
# указываем максимальное количество клиентов, которые могут подключаться к серверу
server_socket.listen(5)

print('Server started and listening for connections...')

# создаем список клиентских сокетов
client_sockets = []


# функция для обработки сообщений от клиентов
def handle_message(message, sender_socket):
    # проходимся по списку клиентских сокетов и отправляем сообщение каждому, кроме отправителя
    for client_socket in client_sockets:
        if client_socket != sender_socket:
            client_socket.send(message)


# функция для обработки клиентского подключения
def handle_client(client_socket):
    while True:
        try:
            # принимаем сообщение от клиента
            message = client_socket.recv(1024)
            # если сообщение пустое, то клиент отключился
            if not message:
                break
            # обрабатываем сообщение
            handle_message(message, client_socket)
        except:
            # если возникает ошибка при получении сообщения, то клиент отключился
            break

    # удаляем клиентский сокет из списка
    client_sockets.remove(client_socket)
    client_socket.close()


while True:
    # принимаем подключение клиента
    client_socket, address = server_socket.accept()
    print(f'Connected by {address}')

    # добавляем клиентский сокет в список
    client_sockets.append(client_socket)

    # запускаем новый поток для каждого клиента
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()


# закрываем серверный сокет при завершении программы
server_socket.close()
