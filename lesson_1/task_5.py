# Задагие №5
import subprocess

args = ['ping', 'yandex.ru']

subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

for line in subproc_ping.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))


args_youtube = ['ping', 'youtube.com']

subproc_ping_youtube = subprocess.Popen(args_youtube, stdout=subprocess.PIPE)

for line in subproc_ping_youtube.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))
