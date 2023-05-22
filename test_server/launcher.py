import tkinter as tk
import subprocess

# Создаем окно
root = tk.Tk()
root.title("Launcher")
root.geometry("500x300")

# Функция запуска сервера
def start_server():
    global server_process
    server_process = subprocess.Popen(["python", "server.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)

# Функция запуска клиентского приложения
def start_client():
    global client_processes
    client_process = subprocess.Popen(['python', 'client.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)
    client_processes.append(client_process)

# Функция остановки сервера
def stop_server():
    server_process.terminate()

# Функция закрытия всех клиентских приложений
def stop_clients():
    for process in client_processes:
        process.terminate()

# Создаем кнопки для запуска сервера и клиентского приложения
server_button = tk.Button(root, text="Start Server", command=start_server, width=100, height=2)
client_button = tk.Button(root, text="Start Client", command=start_client, width=100, height=2)
stop_server_button = tk.Button(root, text="Stop Server", command=stop_server, width=100, height=2)
stop_clients_button = tk.Button(root, text="Stop Clients", command=stop_clients, width=100, height=2)

# Размещаем кнопки на окне
server_button.pack(padx=10, pady=10)
client_button.pack(padx=10, pady=10)
stop_server_button.pack(padx=10, pady=10)
stop_clients_button.pack(padx=10, pady=10)

# Инициализируем список процессов клиентских приложений
client_processes = []

# Запускаем главный цикл обработки событий
root.mainloop()
