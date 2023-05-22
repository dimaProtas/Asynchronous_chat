# Задагие №5
import locale

#Проверяю кодировку
def_coding = locale.getpreferredencoding()

print(def_coding)


with open('text.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')
