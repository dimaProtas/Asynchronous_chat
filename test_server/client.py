import socket
import threading

# Имя пользователя для чата
username = input("Enter username: ")

# Адрес и порт сервера
server_host = 'localhost'
server_port = 8888

# Создание сокета для клиента
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключение к серверу
client_socket.connect((server_host, server_port))

# Функция для приема сообщений от сервера
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message == 'USERNAME':
                client_socket.send(username.encode('utf-8'))
            else:
                sender, recipient, message_text = message.split(':')
                if recipient == username or recipient == "all":
                    print(f'{sender}: {message_text}')
        except:
            print("An error occurred!")
            client_socket.close()
            break

# Функция для отправки сообщений на сервер
def send_messages():
    while True:
        recipient = input("Enter recipient username (or 'all' to send to all): ")
        message_text = input("Enter message: ")
        message = f'{username}:{recipient}:{message_text}'
        client_socket.send(message.encode('utf-8'))

# Создание и запуск потоков для отправки и приема сообщений
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
