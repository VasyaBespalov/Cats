from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image(url):
    try:
        response = requests.get(url)  # Делаем запрос по ссылке url и то ,что вернется положим в respons
        response.raise_for_status()  # Для обработки исключений. Если будет ошибка, здесь ее получим
        image_data = BytesIO(response.content)  # Делаем изображение. В переменную кладем обработанное с IO изображение
        img = Image.open(image_data)
        img.thumbnail((600,480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)  # Функция вернет картинку img
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None  # Если все хорошо функция вернет изображение, если ошибка, то ничего не вернет, но напишет ошибку


def set_image():
    img = load_image(url)  # Сюда кладем картинку полученную в функции load_image

    if img:
        label.config(image=img)  # Далее установим полученное img в метку label
        label.image = img  # Чтобы сборщик мусора не удалил картинку


window = Tk()
window.title("Cats")
window.geometry("600x520")

label = Label()
label.pack()

update_button = Button(text="Обновить", command=set_image)
update_button.pack()

url = "https://cataas.com/cat"

set_image()  # Чтобы картинка появилась при запуске проекта

window.mainloop()
