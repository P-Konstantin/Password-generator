# Библиотека random для случайного выбора символа
import random
# Библиотека tkinter для создания графичесого интерфейса
import tkinter
from tkinter import scrolledtext, END
# Библиотека для работы с изображениями
from PIL import ImageTk



# Создаем переменную с возможными символами для пароля
chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


def make_pass():
    '''Функия создания пароля'''
    password = ''
    length = text.get() # получаем длину пароля
    length = int(length) # переводим полученный текст(длину пароля) в число
    # Создаем цикл для создания пароля
    for i in range(length):
        password += random.choice(chars)
    password = password + '\n'
    return password


def working():
    '''Функция запуска работы программы.'''
    output.configure(state='normal')  # Разрешаем ввод
    output.insert(END, make_pass())
    output.yview(END)  # Включаем автоскроллинг


# Создаем окно программы
window = tkinter.Tk()
# Пишем название программы
window.title('Password generator')
# Задаем цвет окна
window['bg'] = '#acb3ff'
# Задаем размер окна программы
window.geometry('360x360')


# Создаем надпись
lb1 = tkinter.Label(window, text='Программа для создания паролей')
# Задаем цвет надписи
lb1['bg'] = '#acb3ff'
# Задаем расположение надписи
lb1.place(x=10, y=10)


lb2 = tkinter.Label(window, text='Длина пароля:')
lb2['bg'] = '#acb3ff'
lb2.place(x=10, y=30)


# Создаем текстовое поле для ввода длины пароля
text = tkinter.Entry(window, width=10)
# Задаем расположение текствого поля
text.place(x=100, y=30)


# Создаем кнопку для запуска работы программы
btn = tkinter.Button(window, width=26, height=2, text='Создать', command=working)
# Задаем цвет кнопки
btn['bg'] = '#acb3ff'
# Задаем расположение кнопки
btn.place(x=10, y=55)


# Создаем поле для вывода текста
output = tkinter.scrolledtext.ScrolledText(window, width=40, height=15, state='normal')
# Задаем расположение поля вывода
output.place(x=10, y=100)


# Открываем изображение
image = ImageTk.PhotoImage(file='images/image.png')
# Помещаем изображение в tkinter
picture = tkinter.Label(window, image=image)
# Задаем расположение картинки
picture.place(x=220, y=15)
# Задаем цвет вокруг изображения
picture['bg'] = '#acb3ff'


# Создаем бесконечный цикл отображения окна программы
window.mainloop()